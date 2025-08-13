class TrainTimeCard extends HTMLElement {
  set hass(hass) {
    const entityId = this.config.entity;
    const entity = hass.states[entityId];

    if (!entity) {
      this.innerHTML = `<ha-card><div style="padding: 16px;">Sensor introuvable</div></ha-card>`;
      return;
    }

    const trains = entity.attributes.trains || [];
    const station = entity.attributes.station_name || this.config.entity;

    let trainsHtml = "";
    if (trains.length === 0) {
      trainsHtml = "<li>Aucun train disponible</li>";
    } else {
      trains.forEach(train => {
        let time = train.time ? new Date(train.time).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}) : "Inconnue";
        trainsHtml += `<li>🚆 ${train.train_number || "??"} → ${train.destination || "??"} à ${time}</li>`;
      });
    }

    this.innerHTML = `
      <ha-card>
        <div style="padding: 16px; font-family: sans-serif;">
          <h2 style="margin: 0 0 8px 0;">🚉 Gare: ${station}</h2>
          <ul style="padding-left: 20px; margin: 0;">
            ${trainsHtml}
          </ul>
        </div>
      </ha-card>
    `;
  }

  setConfig(config) {
    if (!config.entity) {
      throw new Error("Vous devez spécifier une entité pour la carte");
    }
    this.config = config;
  }

  getCardSize() {
    return 1;
  }
}

customElements.define('traintime-card', TrainTimeCard);

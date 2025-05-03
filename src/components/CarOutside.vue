<script>
export default {
  data() {
    return {
      images: ['out-1.png', 'out-2.png', 'out-3.png', 'out-4.png', 'out-5.png', 'out-6.png'],
      currentIndex: 0,
      hotspots: [
        {
          id: 1,
          index: 0,
          top: '40%',
          left: '55%',
          width: '350px',
          height: '250px',
          part: 'Door',
          pdf: 'doors.pdf',
          clicked: false
        },
        {
          id: 2,
          index: 0,
          top: '60%',
          left: '47%',
          width: '130px',
          height: '200px',
          part: 'Wheel',
          pdf: 'wheels-and-tyres.pdf',
          clicked: false
        },
        {
          id: 3,
          index: 0,
          top: '58%',
          left: '72%',
          width: '100px',
          height: '170px',
          part: 'Wheel',
          pdf: 'wheels-and-tyres.pdf',
          clicked: false
        },
        {
          id: 4,
          index: 0,
          top: '55%',
          left: '10%',
          width: '500px',
          height: '200px',
          part: 'Frontal',
          pdf: 'assistant-frontal.pdf',
          clicked: false
        },
        {
          id: 6,
          index: 0,
          top: '27%',
          left: '42%',
          width: '70px',
          height: '70px',
          part: 'Frontal glass',
          pdf: 'assistant-frontal.pdf',
          clicked: false
        },
        {
          id: 5,
          index: 0,
          top: '39%',
          left: '57%',
          width: '80px',
          height: '40px',
          part: 'Mirror',
          pdf: 'assistant-frontal.pdf',
          clicked: false
        },
        {
          id: 1,
          index: 1,
          top: '40%',
          left: '25%',
          width: '350px',
          height: '250px',
          part: 'Door',
          pdf: 'doors.pdf',
          clicked: false
        },
        {
          id: 2,
          index: 1,
          top: '60%',
          left: '45%',
          width: '130px',
          height: '200px',
          part: 'Wheel',
          pdf: 'wheels-and-tyres.pdf',
          clicked: false
        },
        {
          id: 3,
          index: 1,
          top: '58%',
          left: '22%',
          width: '100px',
          height: '170px',
          part: 'Wheel',
          pdf: 'wheels-and-tyres.pdf',
          clicked: false
        },
        {
          id: 4,
          index: 1,
          top: '39%',
          left: '27%',
          width: '80px',
          height: '40px',
          part: 'Mirror',
          pdf: 'mirrors.pdf',
          clicked: false
        },
        {
          id: 4,
          index: 1,
          top: '39%',
          left: '57%',
          width: '500px',
          height: '300px',
          part: 'Back',
          pdf: 'assistant-back.pdf',
          clicked: false
        },
      ],
      showPdfPopup: false,
      currentPdf: ''
    }
  },
  methods: {
    nextImage() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
    },
    prevImage() {
      this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
    },
    handleHotspotClick(hotspot) {
      if (hotspot.pdf) {
        // Cierra primero el popup para forzar reinicio
        this.showPdfPopup = false;
        
        // Usa nextTick para asegurar que el DOM se actualizó
        this.$nextTick(() => {
          this.currentPdf = hotspot.pdf;
          this.showPdfPopup = true;
        });
      } else {
        alert(`No hay PDF disponible para ${hotspot.part}`);
      }
    },
    closePdfPopup() {
      this.showPdfPopup = false;
    }
  },
  computed: {
    currentImage() {
      return new URL(`../assets/${this.images[this.currentIndex]}`, import.meta.url).href;
    },
    visibleHotspots() {
      return this.hotspots.filter(hotspot => hotspot.index === this.currentIndex);
    },
    pdfPath() {
        if (!this.currentPdf) return null;
        return `/pdfs/${this.currentPdf}`;
    }
  }
}
</script>

<template>
    <div class="fullscreen-container">
      <!-- Imagen FULLSCREEN -->
      <img :src="currentImage" :alt="`Image ${currentIndex + 1}`" class="fullscreen-image">
      
      <!-- Botones de navegación -->
      <button class="nav-button left" @click="prevImage">
        &lt;
      </button>
      <button class="nav-button right" @click="nextImage">
        &gt;
      </button>
      
      <!-- Hotspots interactivos -->
      <button
        v-for="hotspot in visibleHotspots"
        :key="hotspot.id"
        class="hotspot"
        :style="{
          top: hotspot.top,
          left: hotspot.left,
          width: hotspot.width,
          height: hotspot.height,
        }"
        @click="handleHotspotClick(hotspot)"
        :title="`Ver ${hotspot.part}`"
      ></button>
      
      <!-- Popup de PDF con solución completa -->
      <div v-if="showPdfPopup" class="pdf-popup">
        <div class="pdf-popup-content">
          <button class="close-btn" @click="closePdfPopup">×</button>
          <iframe 
            :key="'pdf-' + currentPdf"
            :src="pdfPath" 
            class="pdf-iframe"
            frameborder="0"
          ></iframe>
          <p class="pdf-title">{{ currentPdf }}</p>
        </div>
      </div>
    </div>
  </template>

<style scoped>
/* Estilos FULLSCREEN */
.fullscreen-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  z-index: 1;
}

.fullscreen-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  z-index: 0;
}

/* Botones de navegación */
.nav-button {
  position: fixed;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  font-size: 28px;
  cursor: pointer;
  z-index: 1001;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.3s ease;
}

.nav-button:hover {
  background: rgba(0, 0, 0, 0.8);
  transform: translateY(-50%) scale(1.1);
}

.left {
  left: 30px;
}

.right {
  right: 30px;
}

/* Hotspots */
.hotspot {
  position: absolute;
  background-color: rgba(255, 255, 0, 0.3);
  background-color: transparent;
  border: 2px dashed #ffcc00;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.3s ease;
  z-index: 100;
  padding: 0;
  margin: 0;
  outline: none;
}

.hotspot:hover {
  background-color: rgba(255, 255, 255, 0.5);
  transform: scale(1.1);
}

/* Popup PDF */
.pdf-popup {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 2000;
}

.pdf-popup-content {
    background-color: white;
    position: relative;
    width: 90%;
    max-width: 900px;
    height: 80%;
    max-height: 90vh;
    border-radius: 8px;
    padding: 5px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
}

.close-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    background: none;
    border: none;
    font-size: 28px;
    cursor: pointer;
    cursor: #333;
    z-index: 2001;
}

.close-btn:hover {
    color: #000;
}

.pdf-iframe {
  width: 100%;
  height: calc(100% - 30px);
  margin-top: 10px;
}

.pdf-title {
  position: absolute;
  bottom: 10px;
  left: 20px;
  font-size: 14px;
  color: #666;
}

/* Responsive */
@media (max-width: 768px) {
  .nav-button {
    width: 50px;
    height: 50px;
    font-size: 24px;
  }
  .left {
    left: 15px;
  }
  .right {
    right: 15px;
  }
  
  .hotspot {
    width: 40px !important;
    height: 40px !important;
  }
  
  .pdf-popup-content {
    width: 95%;
    height: 95%;
    padding: 15px;
  }
  
  .pdf-iframe {
    height: calc(100% - 25px);
  }
}
</style>
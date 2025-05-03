<script>
export default {
  data() {
    return {
      hotspots: [
        {
          id: 1,
          top: '30%',
          left: '25%',
          width: '50px',
          height: '50px',
          part: 'Motor',
          clicked: false
        },
        {
          id: 2,
          top: '50%',
          left: '40%',
          width: '60px',
          height: '30px',
          part: 'Puerta',
          clicked: false
        },
        {
          id: 3,
          top: '70%',
          left: '35%',
          width: '40px',
          height: '40px',
          part: 'Rueda',
          clicked: false
        }
        // Añade más áreas según necesites
      ]
    }
  },
  methods: {
    handleClick(hotspot) {
      hotspot.clicked = true
      this.$emit('part-clicked', hotspot.part)
      setTimeout(() => hotspot.clicked = false, 500)
    }
  }
}
</script>

<template>
  <div class="car-container">
    <!-- Imagen del coche -->
    <img src="../assets/out-1.png" alt="Coche" class="car-image">
    
    <!-- Botones interactivos -->
    <button
      v-for="hotspot in hotspots"
      :key="hotspot.id"
      class="hotspot"
      :style="{
        top: hotspot.top,
        left: hotspot.left,
        width: hotspot.width,
        height: hotspot.height,
      }"
      @click="handleClick(hotspot)"
      :class="{ 'hotspot-clicked': hotspot.clicked }"
      :title="`Haz clic para ver ${hotspot.part}`"
    ></button>
  </div>
</template>

<style scoped>
.car-container {
  position: relative;
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
}

.car-image {
  width: 100%;
  display: block;
}

.hotspot {
  position: absolute;
  background-color: rgba(255, 255, 0, 0.3);
  border: 2px dashed #ffcc00;
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.3s ease;
  z-index: 10;
  padding: 0;
}

.hotspot:hover {
  background-color: rgba(255, 200, 0, 0.5);
  transform: scale(1.1);
}

.hotspot-clicked {
  background-color: rgba(0, 255, 0, 0.5) !important;
  transform: scale(1.2);
  border: 2px solid #00ff00;
}
</style>
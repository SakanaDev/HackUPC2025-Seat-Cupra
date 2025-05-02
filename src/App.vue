<script>
import CarOutside from './components/CarOutside.vue';
import CarInside from './components/CarInside.vue';

export default {
  data() {
    return {
      isOutside: true,
    }
  },
  components: {
    CarOutside,
    CarInside,
  }
}
</script>

<template>
  <header>
    <a href="">
      <img src="https://www.cupraofficial.es/etc.clientlibs/cupra-website/components/clientlibs/resources/icons/logos/logo-cupra.svg" alt="">
    </a>
  </header>
  <div class="car-container">
    <CarOutside v-if="isOutside"></CarOutside>
    <CarInside v-if="!isOutside"></CarInside>
  </div>
  <div class="options">
    <button @click="isOutside=true">car</button>
    <button @click="isOutside=false">inside</button>
  </div>
</template>

<style scoped>
header {
  position: relative;
  background-color: black;
  padding: 0 16px;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>

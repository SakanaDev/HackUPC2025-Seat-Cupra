<script>
export default {
  props: {
    top: { type: String, default: '100px' },
    left: { type: String, default: '50px' },
    bottom: { type: String, default: '' },
    right: { type: String, default: '' },
    isDashed: { type: Boolean, default: false },
    width: { type: String, default: '100px' },
    height: { type: String, default: '50px' }
  },
  computed: {
    btnStyle() {
      return {
        position: 'fixed',
        top: this.top,
        left: this.left,
        bottom: this.bottom,
        right: this.right,
        width: this.width,
        height: this.height,
        border: this.isDashed ? '2px dashed gray' : '2px solid black',
        backgroundColor: 'rgba(102, 51, 153, 0.3)', // Morado semitransparente
        zIndex: '1002',
        cursor: 'pointer',
        borderRadius: '5px'
      }
    }
  }
}
</script>

<template>
  <button :style="btnStyle" class="custom-btn"></button>
</template>

<style scoped>
/* Estilos base como respaldo */
.custom-btn {
  position: fixed;
  z-index: 1002;
}
</style>
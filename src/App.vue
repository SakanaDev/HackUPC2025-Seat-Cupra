<script>
import VideoPro from './components/VideoPro.vue'
export default {
    components:{
        VideoPro,
    },
    data() {
    return {
      endVideo: false,
    }
  }
}

</script>

<template>
    <VideoPro v-if="!endVideo" @video-ended="endVideo = true" />
    <h1>test</h1>
</template>

<style scoped>

</style>

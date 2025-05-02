<script>
export default {
    data() {
        return {
            imageArray: ['out-1.png', 'out-2.png', 'out-3.png', 'out-4.png', 'out-5.png', 'out-6.png'],
        }
    },

}
</script>

<template>
    <img v-for="image in imageArray" :src="`@/assets/${image}`" :alt="image">
</template>

<style scoped>
</style>
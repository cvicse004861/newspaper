<template>
  <div class="map-container">
    <el-amap></el-amap>
  </div>
</template>

<script>
const actualGantry = require('./assets/node/gantry.actual.22030201.json')
const virtualGantry = require('./assets/node/gantry.virtual.22030201.json')
const nodeRef = require('./assets/node/ref.22030201.json')
const service = require('./assets/node/service.22030201.json')
const station = require('./assets/node/station.22030201.json')

export default {
  name: "VersionMap",
  methods: {
  }
}
</script>
<style scoped>
.map-container {
  width: 800px;
  height: 600px;
}
</style>

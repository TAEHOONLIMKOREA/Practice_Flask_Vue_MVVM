<template>
  <div class="home">
    <HeaderComponent/>
    <img alt="Vue logo" src="../assets/logo.png">
    <PingComponent/>
  </div>
</template>

<script>
// @ is an alias to /src
import HeaderComponent from '../components/layout/HeaderComponent.vue'
import PingComponent from '../components/layout/PingComponent.vue'

export default {
  name: 'HomeView',
  components: {
    HeaderComponent,
    PingComponent,
  }
}
</script>

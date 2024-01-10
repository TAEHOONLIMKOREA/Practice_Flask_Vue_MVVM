<template>
  <div class="home">
    <HeaderComponent/>
    <img alt="Vue logo" src="../assets/logo.png">
  </div>
</template>

<script>
// @ is an alias to /src
import HeaderComponent from '../components/layout/HeaderComponent.vue'

export default {
  name: 'HomeView',
  components: {
    HeaderComponent,
  }
}
</script>

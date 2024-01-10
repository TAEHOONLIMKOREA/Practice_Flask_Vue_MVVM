<!-- eslint-disable-next-line -->
<template>
  <h1>{{ msg }}</h1>
</template>
<script>
export default {
  name: 'PingComponent',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      fetch(path)
        .then((response) => {
          if (!response.ok) {
            console.error('Error fetching data:');
            throw new Error(`HTTP error! Status: ${response.status}`);        
          }
          return response.text();
        })
        .then((data) => {
          this.msg = data;
        })
        .catch((error) => {
          console.error('Error fetching data:', error);
          this.msg = error;
        });
      },
    },
  created() {
    this.getMessage();      
  }
};
</script>
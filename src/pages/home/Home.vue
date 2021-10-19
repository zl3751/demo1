<template>
  <div>
    <h1 class="home">home</h1>
    <button @click="handleStartClick">
      Start Training
    </button>
    <button @click="handleQuery">Query</button>
      <p>{{query_content}}</p>
    <button @click="handlePositiveClick">Positive</button>
    <button @click="handleNegativeClick">Negative</button>
  </div>
</template>

<script>
// import QueryBox from './components/QueryBox.vue'

export default ({
  name: 'Home',
  data: function () {
    return {
      query_content: '',
      query_idx: -1,
      started: false
      // counter: 0
    }
  },
  methods: {
    handleStartClick: function () {
      this.started = true
      this.$ajax.get('/pre', {}).then(res => {
        console.log('good')
      })
    },
    handlePositiveClick: function () {
      this.$ajax.post('/label', {'label': 1, 'idx': this.query_idx}).then(res => {
        console.log(res.data.performance)
      })
    },
    handleNegativeClick: function () {
      this.$ajax.post('/label', {'label': 0, 'idx': this.query_idx}).then(res => {
        console.log(res.data.performance)
      })
    },
    handleQuery: function () {
      this.$ajax.get('/query', {}).then(res => {
        this.query_content = res.data.content
        this.query_idx = res.data.idx
        console.log(res.data.oracle)
      })
    }
    // receiveData () {
    //   this.$ajax.post('/test', {'msg': 'get req'}).then(res => {
    //     this.query_data = JSON.parse(res.data.query)
    //   })
    // }
  },
  components: {
    // QueryBox
  }
})
</script>

<style>
</style>

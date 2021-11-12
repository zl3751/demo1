<template>
  <div id='home' class='home'>
    <h1 id='homeheader' class="home">active learner</h1>
    <button @click="handleQuery">Query</button>
      <p>{{query_content}}</p>
    <button class='button_p' @click="handlePositiveClick">Positive</button>
    <button class='button_n' @click="handleNegativeClick">Negative</button><br>
    <br><br><hole class='graph' :data='uncertainties'></hole>
  </div>
</template>

<script>
import hole from './components/hole.vue'

export default ({
  name: 'Home',
  data: function () {
    return {
      query_content: '',
      query_idx: -1,
      uncertainties: [],
      performance: []
    }
  },
  computed: {
    uncertainty () {
      return this.data
    }
  },
  methods: {
    handlePositiveClick: function () {
      this.$ajax.post('/model/label', {'label': 1, 'idx': this.query_idx}).then(res => {
        this.uncertainties.push(res.data.uncertainty)
        this.performance = res.data.performance
      })
    },
    handleNegativeClick: function () {
      this.$ajax.post('/model/label', {'label': 0, 'idx': this.query_idx}).then(res => {
        console.log('n update')
      })
    },
    handleQuery: function () {
      this.$ajax.get('/model/query', {}).then(res => {
        this.query_content = res.data.content
        this.query_idx = res.data.index
        console.log(res.data.oracle)
      })
    }
  },
  mounted () {
    //
  },
  components: {
    hole
  }
})
</script>

<style>
  /* .graph {
    position: absolute;
    left: 38%;
    outline: 2px solid black;
    /* outline-offset: 1px; */
</style>

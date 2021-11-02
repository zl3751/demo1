<template>
  <div>
    <h1 class="home">active learner</h1>
    <button @click="handleStartClick">
      Start Training
    </button>
    <button @click="handleQuery">Query</button>
      <p>{{query_content}}</p>
    <button @click="handlePositiveClick">Positive</button>
    <button @click="handleNegativeClick">Negative</button>
    <score-chart v-if='loaded'
                :chartData='chartData'
                :options='options'/>
  </div>
</template>

<script>
import ScoreChart from './components/ScoreChart'

export default ({
  name: 'Home',
  data: function () {
    return {
      query_content: '',
      query_idx: -1,
      started: false,
      loaded: false,
      chartData: {
        labels: [],
        datasets: [{
          label: 'Score',
          data: []}
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  methods: {
    async handleStartClick () {
      this.started = true
      await this.$ajax.get('/model/pre', {}).then(res => {
        const initScore = res.data.newscore
        this.updateChartData(initScore)
      })
      this.loaded = true
    },
    handlePositiveClick: function () {
      this.$ajax.post('/model/label', {'label': 1, 'idx': this.query_idx}).then(res => {
        console.log('p update')
        this.updateChartData(res.data.performance)
        console.log(this.chartData.datasets[0].data)
        console.log(this.chartData.labels)
      })
    },
    handleNegativeClick: function () {
      this.$ajax.post('/model/label', {'label': 0, 'idx': this.query_idx}).then(res => {
        console.log('n update')
        this.updateChartData(res.data.performance)
        console.log(this.chartData.datasets[0].data)
        console.log(this.chartData.labels)
      })
    },
    handleQuery: function () {
      this.$ajax.get('/model/query', {}).then(res => {
        this.query_content = res.data.content
        this.query_idx = res.data.idx
        console.log(res.data.oracle)
      })
    },
    updateChartData: function (newData) {
      const len = this.chartData.datasets[0].data.length
      this.chartData.datasets[0].data.push(newData)
      this.chartData.labels.push(len.toString())
    }
  },
  mounted () {
    //
  },
  components: {
    ScoreChart
  }
})
</script>

<style>
</style>

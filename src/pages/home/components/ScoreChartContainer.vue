<template>
  <div class='scorechartcontainer'>
    <score-chart v-if='loaded'
                :chartdata='chartdata'
                :options='options'/>
  </div>
</template>

<script>
import ScoreChart from './ScoreChart.vue'

export default {
  name: 'ScoreChartContainer',
  components: { ScoreChart },
  data: () => ({
    loaded: false,
    chartdata: {
      labels: [0, 1, 2, 3, 4, 5, 6, 7],
      datasets: [
        {
          label: 'Per',
          data: [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false
    }
  }),
  mounted () {
    this.loaded = true
    this.$ajax.get('/model/performance', {}).then(res => {
      console.log('HelloAjax')
    })
  }
}
</script>

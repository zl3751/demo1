<script>
import {Line, mixins} from 'vue-chartjs'
const {reactiveProp} = mixins

export default {
  name: 'ScoreChart',
  extends: Line,
  mixins: [reactiveProp],
  props: ['options'],
  mounted () {
    this.renderChart(this.chartData, this.options)
  }
}
</script>

//  name: 'ScoreChart',
//   extends: Line,
//   props: {
//     chartdata: {
//       type: Object,
//       default: null
//     },
//     options: {
//       type: Object,
//       default: null
//     }
//   },
//   mounted () {
//     this.renderChart(this.chartdata, this.options)
//   }

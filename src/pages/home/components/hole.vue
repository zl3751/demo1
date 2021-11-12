<template>
  <div id='container' class='svg-container' align='center'>
    <svg :width='width + margin.left + margin.right'
      :height='height + margin.top + margin.bottom'>
      <g :transform="`translate(${margin.left}, ${margin.top})`">
        <g v-for='r in data' :key="r.epoch"
          :transform="`translate(${groupX(r.epoch)}, 0)`"
        >
          <circle v-for='point in r.values' :key='point.id'
            :cx='pointX()' :cy='pointY(point.value)'
            r='3' fill='steelblue'/>
        </g>
        <!--X axis-->
        <g v-bind:transform="`translate(0,${height})`" font-family="sans-serif">
        <g
          v-for="run in data"
          v-bind:key="run.epoch"
          v-bind:transform="`translate(${
            groupX(run.epoch) + groupX.bandwidth() / 2
          })`"
        >
          <text text-anchor="middle" y="20">Epoch {{ run.epoch }}</text>
        </g>
        <!-- y-axis -->
        <!-- <g font-family="sans-serif">
          <g
            v-for="tick in pointY.ticks(10)"
            v-bind:key="tick"
            v-bind:transform="`translate(0,${pointY(tick)})`"
          >
            <line x1="-6" stroke="black"/>
            <text text-anchor="end" dominant-baseline="middle" x="-8">{{tick}}</text>
          </g>
        </g> -->
      </g>
      </g>
    </svg>
  </div>
</template>

<script>
import * as d3 from 'd3'

export default ({
  name: 'graph',
  props: {
    data: Array
  },
  data: function () {
    const margin = {top: 10, right: 10, bottom: 40, left: 40}
    const width = 600 - margin.left - margin.right
    const height = 400 - margin.top - margin.bottom
    return {width, height, margin}
  },
  computed: {
    groupX () {
      return d3.scaleBand()
        .domain(this.data.map(d => {
          return d.epoch
        }))
        .range([0, this.width])
        .paddingOuter(0.1)
        .paddingInner(0.5)
    },
    pointX () {
      return d3.randomInt(0, this.groupX.bandwidth())
    },
    pointY () {
      return d3.scaleLinear().domain([0, 1]).range([this.height, 0])
    }
  }
})
</script>

<style>
</style>

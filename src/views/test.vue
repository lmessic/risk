<template>
 <div class="chartNum">
    <h3 class="orderTitle">订单总量</h3>
    <div class="box-item">
      <li class="number-item"
        v-for="(item,index) in orderNum"
        :key="index"
      >
        <span>
          <i ref="numberItem">0123456789</i>
        </span>
      </li>
    </div>
   </div>
</template>
<script>
export default {
  data () {
    return {
      orderNum: ['0', '0', '0']
    }
  },
  mounted () {
    this.increaseNumber()
    this.orderNum = [4, 2, 0]
  },
  methods: {
    increaseNumber () {
      this.timer = setInterval(() => {
        this.setNumberTransform()
      }, 1000)
    },
    // 设置文字滚动
    setNumberTransform () {
      const numberItems = this.$refs.numberItem // 拿到数字的ref，计算元素数量
      const numberArr = this.orderNum.filter(item => !isNaN(item))
      // 结合CSS 对数字字符进行滚动
      for (let index = 0; index < numberItems.length; index++) {
        const elem = numberItems[index]
        const num = numberArr[index]
        elem.style.transform = `translate(-50%, -${num * 10}%)`
      }
    }
  }
}
</script>
<style scoped lang='less'>
  /*订单总量滚动数字设置*/
 .box-item {
  position: relative;
  height: 100px;
  font-size: 54px;
  line-height: 41px;
  text-align: center;
  list-style: none;
  color: #2D7CFF;
  writing-mode: vertical-lr;
  text-orientation: upright;
  /*文字禁止编辑*/
  -moz-user-select: none; /*火狐*/
  -webkit-user-select: none; /*webkit浏览器*/
  -ms-user-select: none; /*IE10*/
  -khtml-user-select: none; /*早期浏览器*/
  user-select: none;
  /* overflow: hidden; */
 }
 /*滚动数字设置*/
 .number-item {
  width: 41px;
  height: 75px;
  background: #ccc;
  list-style: none;
  margin-right: 5px;
  background:rgba(250,250,250,1);
  border-radius:4px;
  border:1px solid rgba(221,221,221,1);
  & > span {
   position: relative;
   display: inline-block;
   margin-right: 10px;
   width: 100%;
   height: 100%;
   writing-mode: vertical-rl;
   text-orientation: upright;
   overflow: hidden;
   & > i {
      font-style: normal;
      position: absolute;
      top: 11px;
      left: 50%;
      transform: translate(-50%,10%);
      transition: transform 1s ease-in-out;
      letter-spacing: 10px;
    }
  }
 }
 .number-item:last-child {
  margin-right: 0;
 }
</style>

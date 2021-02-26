<template>
  <div class="contain">
    <div class="top">
      <el-image :src="require('../assets/logo_one.png')"></el-image>
      <el-image :src="require('../assets/logo_two.png')"></el-image>
      <div class="top-content">
        <el-image :src="require('../assets/title.png')"></el-image>
        <div class="intro">
          创新实验室（Finlab）负责开展先导性课题和项目进行产品原型孵化和示范应用打造，推动业务与技术创新
        </div>
      </div>
      <div class="back-img"></div>
    </div>
    <div class="middle">
      <el-row>
        <el-col :span="8" class="module">
          <el-image :src="require('../assets/part_one.png')"></el-image>
          <div class="part">
            <span>Part</span>
            <span>1</span>
          </div>
          <transition name="icon_text1">
            <p v-show="textFlag">负责ABCDMIX等前沿技术跟踪和研究</p>
          </transition>
        </el-col>
        <el-col :span="8" class="module">
          <el-image :src="require('../assets/part_two.png')"></el-image>
          <div class="part">
            <span>Part</span>
            <span>2</span>
          </div>
          <transition name="icon_text2">
            <p v-show="textFlag">负责金融科技行业分析、跟踪与研究</p>
          </transition>
        </el-col>
        <el-col :span="8" class="module">
          <el-image :src="require('../assets/part_three.png')"></el-image>
          <div class="part">
            <span>Part</span>
            <span>3</span>
          </div>
          <transition name="icon_text3">
            <p v-show="textFlag">负责黑科技公司与产学研用一体化合作</p>
          </transition>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="8" class="module">
          <el-image :src="require('../assets/part_four.png')"></el-image>
          <div class="part">
            <span>Part</span>
            <span>4</span>
          </div>
          <transition name="icon_text4">
            <p v-show="textFlag">负责基础技术中心知识产权相关工作</p>
          </transition>
        </el-col>
        <el-col :span="8" class="module">
          <el-image :src="require('../assets/part_five.png')"></el-image>
          <div class="part">
            <span>Part</span>
            <span>5</span>
          </div>
          <transition name="icon_text5">
            <p v-show="textFlag">参与母行与金科公司重点项目技术攻关</p>
          </transition>
        </el-col>
        <el-col :span="8" class="module">
          <el-image :src="require('../assets/part_six.png')"></el-image>
          <div class="part">
            <span>Part</span>
            <span>6</span>
          </div>
          <transition name="icon_text6">
            <p v-show="textFlag">承担基础技术创新能力引入的统筹工作</p>
          </transition>
        </el-col>
      </el-row>
      <el-row type="flex" class="row-bg">
        <el-col :span="10" v-for="(item,index) in boxList" :key="index">
          <div class="box" @click="toDetail">
            <div class="box-bk" :class="setBk(item.type)"></div>
            <div class="content">
              <h4>{{ item.title }}</h4>
              <div class="text">{{ item.text }}</div>
              <div class="operate">
                <span>详情</span>
                <i class="el-icon-right"></i>
              </div>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      boxList: [
        {
          id: '1',
          type: 'bk-one',
          title: '零售客户风险限额',
          text: '零售客户风险限额模型引入了经济学中的人力资本理论，行为认知理论、金融素养理论以及风险偏好理论进行跨科学融合创新...'
        },
        {
          id: '2',
          type: 'bk-two',
          title: '零售客户风险限额',
          text: '零售客户风险限额模型引入了经济学中的人力资本理论，行为认知理论、金融素养理论以及风险偏好理论进行跨科学融合创新...'
        },
        {
          id: '3',
          type: 'bk-three',
          title: '零售客户风险限额',
          text: '零售客户风险限额模型引入了经济学中的人力资本理论，行为认知理论、金融素养理论以及风险偏好理论进行跨科学融合创新...'
        },
        {
          id: '4',
          type: 'bk-four',
          title: '零售客户风险限额',
          text: '零售客户风险限额模型引入了经济学中的人力资本理论，行为认知理论、金融素养理论以及风险偏好理论进行跨科学融合创新...'
        }
      ],
      textFlag: false
    }
  },
  computed: {
    setBk () {
      return function (val) {
        return val
      }
    }
  },
  mounted () {
    const demo = document.querySelector('.top')
    const length = document.querySelector('.top').offsetWidth / 2
    const height = document.querySelector('.top').offsetHeight / 2
    const background = document.querySelector('.back-img')
    demo.addEventListener('mousemove', function (e) {
      const x = (length - e.pageX) / 10
      const y = (height - e.pageY) / 10
      background.style.transform = `translate(${x}px, ${y}px)`
    })
    this.setScroll()
  },
  methods: {
    toDetail () {
      this.$router.push({
        path: '/detail'
      })
    },
    setScroll () {
      const scrollFunc = () => {
        const elTop = document.querySelector('.top').offsetHeight / 2
        const elBg = document.querySelector('.row-bg').offsetHeight
        if (window.pageYOffset > elTop) {
          this.textFlag = true
        } else {
          this.textFlag = false
        }
        if (window.pageYOffset > elBg) {
          this.textFlag = false
        }
      }
      if (document.querySelector('.top') !== undefined && document.querySelector('.row-bg') !== undefined) {
        window.onmousewheel = document.onmousewheel = scrollFunc
      }
      // document.onscroll = function func (e) {
      //   console.log(document.documentElement.scrollTop)
      // }
    }
  }
}
</script>
<style lang="less" scoped>
.contain {
  width: 100%;
  height: 100%;
  .top {
    height: calc(100vh - 60px);
    padding: 60px 0 0 60px;
    position: relative;
    overflow-x: hidden;
    overflow-y: hidden;
    z-index: 1;
    .top-content {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      text-align: center;
      color: #fff;
      z-index: 1;
      .intro {
        margin-top: 60px;
        font-size: 36px;
        text-shadow: 5px 5px 5px #888484;
      }
    }
    .back-img {
      position: absolute;
      top: -5%;
      left: -5%;
      width: 110%;
      height: 110%;
      z-index: -1;
      background: url('../assets/home_virtual.jpg') no-repeat;
      background-size: 100% 100%;
      background-position: center 0;
    }
  }
  .top:hover {
    .back-img {
      animation: animate 8s infinite ease-in-out;
      -webkit-animation: animate 8s infinite ease-in-out;
      -moz-animation: animate 8s infinite ease-in-out;
    }
  }
  @keyframes animate {
    0% {
      background: url('../assets/home_virtual.jpg') no-repeat;
      background-size: 100% 100%;
      background-position: center 0;
    }
    50% {
      background: url('../assets/home_real.jpg') no-repeat;
      background-size: 100% 100%;
      background-position: center 0;
    }
  }
  .middle {
    padding: 0 15%;
    .el-row:nth-child(1) {
      margin-top: 100px;
    }
    .el-row:nth-child(2) {
      margin: 100px 0;
    }
    .module {
      min-width: 275px;
      min-height: 210px;
      text-align: center;
      .part {
        font-size: 24px;
        font-weight: bold;
        line-height: 33px;
        margin-top: 30px;
      }
      .part > span:nth-last-child(1) {
        color: #2E7FEF;
      }
    }
    .row-bg {
      justify-content: space-around;
      flex-wrap: wrap;
      margin-top: 30px;
      .el-col {
        margin-bottom: 16px;
      }
    }
    .box {
      width: 100%;
      height: 580px;
      padding: 0;
      box-shadow: 2px 4px 8px 0px rgba(0, 0, 0, 0.13);
      transition: all 1s;
      -webkit-transition: all 1s;
      cursor: pointer;
      .box-bk {
        width: 100%;
        height: 360px;
      }
      .bk-one {
        background: url('../assets/bk_one.jpg') no-repeat;
        background-size: cover;
        background-position: center 0;
      }
      .bk-two {
        background: url('../assets/bk_two.jpeg') no-repeat;
        background-size: cover;
        background-position: center 0;
      }
      .bk-three {
        background: url('../assets/bk_three.jpg') no-repeat;
        background-size: cover;
        background-position: center 0;
      }
      .bk-four {
        background: url('../assets/bk_four.jpg') no-repeat;
        background-size: cover;
        background-position: center 0;
      }
      .content {
        padding: 5px 30px;
        .text {
          width: 320px;
          font-size: 14px;
          color: #7D828A;
          line-height: 24px;
        }
        .operate {
          text-align: right;
          font-size: 14px;
          line-height: 50px;
          span, i {
            cursor: pointer;
          }
          i {
            color: #1657D9;
          }
        }
        h4 {
          font-size: 24px;
        }
      }
    }
    .box:hover {
      transform: translate(-10px -10px);
      -webkit-transform:translate(-10px,-10px);
      box-shadow: 9px 15px 13px 0px rgba(0, 0, 0, 0.1);
      .operate {
        color: #1657D9;
      }
    }
  }
  .icon_text1-enter-active, .icon_text2-enter-active, .icon_text3-enter-active,
  .icon_text4-enter-active, .icon_text5-enter-active, .icon_text6-enter-active {
    transition: all 4s ease;
    -webkit-transition: all 4s ease;
  }
  .icon_text1-leave-active, .icon_text2-leave-active, .icon_text3-leave-active,
  .icon_text4-leave-active, .icon_text5-leave-active, .icon_text6-leave-active {
    transition: all 1 ease;
    -webkit-transition: all 1 ease;
  }
  .icon_text1-enter, .icon_text1-leave-to, .icon_text2-enter, .icon_text2-leave-to,
  .icon_text3-enter, .icon_text3-leave-to, .icon_text4-enter, .icon_text4-leave-to,
  .icon_text5-enter, .icon_text5-leave-to, .icon_text6-enter, .icon_text6-leave-to{
    transform: translateY(50px);
    -webkit-transform: translateY(50px);
    opacity: 0;
  }
}
</style>

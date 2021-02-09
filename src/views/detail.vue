<template>
  <div class="contain">
    <div class="anchor">
      <span><el-image :src="require('../assets/logo_one.png')"></el-image></span>
      <span><el-image :src="require('../assets/logo_two.png')"></el-image></span>
      <div class="aside">
        <div
          v-for="(item) in menuList"
          :key="item.id"
          @click="scrollEvent(item)"
          class="divider-text"
          :class="setBorderColor()"
        >
          <span class="aside-text">{{ item.name }}</span>
        </div>
      </div>
      <div class="point-block">
        <el-image :src="require('../assets/logo_three.png')" v-if="numPage===1||numPage===3||numPage===5"></el-image>
        <el-image :src="require('../assets/logo_four.png')" v-else></el-image>
      </div>
    </div>
    <full-page :options="fullOptions" id="fullpage" ref="fullpage">
      <div class="top section">
        <div class="content">
          <div class="title">零售客户风险限额</div>
          <div class="intro">
            零售客户风险限额模型从客户的成长性角度出发，明确了客户可承担的、最大客观的债务总量，实现了客户级风险总量控制
          </div>
          <div class="desc">
            <div v-for="(item, index) in list" :key="index">
              <div class="num-wrapper">
                <span style="opacity: 0; font-size: 30px;">1</span>
                <span style="opacity: 0; font-size: 30px;">0</span>
                <!-- <span>{{ item.num }}</span> -->
                <transition name="num_one">
                  <div class="num_one" v-show="numFlag">
                    <p>1</p>
                    <p>2</p>
                    <p>3</p>
                    <p v-if="item.id == '1'">4</p>
                    <p v-if="item.id == '2'">6</p>
                    <p v-if="item.id == '3'">3</p>
                  </div>
                </transition>
                <transition name="num_two" v-if="item.id==='1'||item.id==='2'">
                  <div class="num_two" v-show="numFlag">
                    <p>1</p>
                    <p>2</p>
                    <p>3</p>
                    <p>4</p>
                    <p>5</p>
                    <p>0</p>
                  </div>
                </transition>
                <transition name="num_three" v-if="item.id==='2'">
                  <div class="num_three" v-show="numFlag">
                    <p>1</p>
                    <p>2</p>
                    <p>3</p>
                    <p>4</p>
                    <p>5</p>
                    <p>6</p>
                    <p>0</p>
                  </div>
                </transition>
                <span class="name" :class="setMargin(item.id)">{{ item.name }}</span>
              </div>
              <div class="text">
                {{ item.desc }}
              </div>
            </div>
          </div>
        </div>
        <div class="back-img"></div>
      </div>
      <el-row class="challenge section">
        <el-col :span="14">
          <transition name="fade">
            <div class="c-left" v-show="challengeFlag">
              <div class="title">背景与挑战</div>
              <p>
                目前母行在普惠金融经营模式和生态布局方面取得了丰硕的成果，业务快速健康发展，尤其是在小微企业主、个体工商户、农村金融等领域。然而，普惠金融业务的快速发展也对风险防控提出了更高的挑战，要求完善模型、数据、工具等风险管理方式，提升风险识别的敏感性和准确性，切实提高风险防控的能力。
              </p>
              <p>
                当前普惠金融和互联网金融快速发展、信贷产品种类激增、居民杠杆率不断上升，多头授信、过度授信是当前风险防控的痛点之一。如何对零售个人客户，尤其是低收入人群、贫困人群等下沉客群进行准确定价，明确这些客户可承担的、最大的、客观的债务总量是当前信贷额度控制的关键问题。只有从客户层面控制、管理信贷额度总量，才能降低违约风险，保证普惠金融的供需双方实现利益共赢，维持商业模式的可持续性。而传统风险限额是产品级的基于客户现时收入的额度，没有考虑客户的成长能力，缺少客户维度的可承担最大债务总量的测定方法，难以把控客户的整体风险限额。
              </p>
            </div>
          </transition>
        </el-col>
        <el-col :span="10" class="bk-five">
          <div class="scaleBk"></div>
          <div class="abstruct">
            <el-image :src="require('../assets/mark_one.png')" v-if="numPage===5"></el-image>
            <el-image :src="require('../assets/mark_two.png')" v-else></el-image>
          </div>
        </el-col>
      </el-row>
      <el-row class="risk section">
        <el-col :span="10"></el-col>
        <el-col :span="14" class="risk-content">
          <transition name="fade-risk">
            <div class="r-right" v-show="riskFlag">
              <div class="title">什么是风险限额</div>
              <p>
                零售客户风险限额模型引入了经济学中的人力资本理论、行为认知理论、金融素养理论以及风险偏好理论进行跨学科融合创新，基于大数据和机器学习算法设计实现了“个人未来经济价值预测”的零售客户风险限额策略，突破了传统的基于现时收入的限额计算方法的局限性。模型从客户的成长性角度出发，综合考虑客户的无形资产的未来价值和有形资产的未来价值来确定客户可承担的最大债务总量，代表了客户各项授信总额所不能够超过的“天花板”，有着跨产品、跨机构的特性。风险限额管理全面实现了客户级风险总量控制，完善了风险管控流程，进一步强化了零售客户的风险管理，对于国内外商业银行和类金融机构具有颠覆性的创新意义。
              </p>
            </div>
          </transition>
          <div class="abstruct">
            <el-image :src="require('../assets/mark_one.png')" v-if="numPage===5"></el-image>
            <el-image :src="require('../assets/mark_two.png')" v-else></el-image>
          </div>
        </el-col>
      </el-row>
      <el-row class="way section">
        <el-col :span="14">
          <transition name="fade-way">
            <div class="c-left" v-show="wayFlag">
              <div class="title">我们的方法</div>
              <p>
                零售客户风险限额设计方案包含两个部分。第一个部分基于劳动经济学的人力资本理论和行为经济学的行为认知理论，从金融资产定价的视角预测零售客户风险限额中无形资产的现金流价值，主要通过客户分群后，对同质化水平较高的特定客群计算其劳动收入未来价值和晋升的潜在收入成长；第二个部分则基于金融学的风险偏好理论，同时考虑行为认知理论，将零售客户视为“企业”，从收益增长的视角预测零售客户风险限额中有形资产的市场价值，包括房屋资产的机会成本和金融资产的市场价值，这两部分合并之后得到零售客户风险限额。
              </p>
              <div class="func"></div>
            </div>
          </transition>
        </el-col>
        <el-col :span="10" class="way-content">
          <div class="abstruct">
            <el-image :src="require('../assets/mark_one.png')" v-if="numPage===5"></el-image>
            <el-image :src="require('../assets/mark_two.png')" v-else></el-image>
          </div>
        </el-col>
      </el-row>
      <div class="video section">
        <div class="abstruct">
          <el-image :src="require('../assets/mark_one.png')" v-if="numPage===5"></el-image>
          <el-image :src="require('../assets/mark_two.png')" v-else></el-image>
        </div>
      </div>
      <el-row class="bottom section">
        <el-col :span="10"></el-col>
        <el-col :span="14" class="bottom-content">
          <transition name="fade-bottom">
            <div class="r-right" v-show="bottomFlag">
              <div class="title">零售客户风险限额</div>
              <p>
                零售客户风险限额模型引入了经济学中的人力资本理论、行为认知理论、金融素养理论以及风险偏好理论进行跨学科融合创新
              </p>
              <el-button size="small" type="primary" @click="question"
                >立即试用</el-button
              >
            </div>
          </transition>
          <div class="abstruct">
            <el-image :src="require('../assets/mark_one.png')" v-if="numPage===5"></el-image>
            <el-image :src="require('../assets/mark_two.png')" v-else></el-image>
          </div>
        </el-col>
      </el-row>
    </full-page>
    <el-dialog
      :visible.sync="dialogVisible"
      width="40%"
      center
      :show-close="false"
      :close-on-click-modal="false"
      class="modal"
    >
      <el-row>
        <el-col :span="2">0</el-col>
        <el-col :span="20" style="text-align: center">{{number}}/10题</el-col>
        <el-col :span="2" style="text-align: right">10</el-col>
      </el-row>
      <el-slider
        v-model="topVal"
        :step="1"
        :show-tooltip="false"
        :max="10"
        range
        disabled
        @input="changeVal"
        class="title-slider"
      ></el-slider>
      <div>
        <div class="question">1. 请问您的工作年限？</div>
        <el-select v-model="selVal" placeholder="请选择" size="mini">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </div>
      <div>
        <div class="question">2. 请问您的性别？</div>
        <el-button type="primary" size="mini" @click="selectBtn">男性</el-button>
        <el-button type="primary" size="mini">女性</el-button>
      </div>
      <div>
        <div class="question">3. 请问您生活在哪里？</div>
        <el-cascader
          v-model="addressVal"
          :options="addOptions"
          @change="handleChange"
          size="mini"
        ></el-cascader>
      </div>
      <div>
        <div class="question">4. 请问您的学历？</div>
        <el-button type="primary" size="mini">博士</el-button>
        <el-button type="primary" size="mini">硕士/本科</el-button>
        <el-button type="primary" size="mini">其它</el-button>
      </div>
      <div>
        <div class="question">5. 请问您从事的行业？</div>
      </div>
      <div>
        <div class="question">6. 请问您大致的月收入？</div>
        <el-slider v-model="incomeVal"></el-slider>
      </div>
      <div>
        <div class="question">7. 请问您是否有房？</div>
        <el-button type="primary" size="mini">是</el-button>
        <el-button type="primary" size="mini">否</el-button>
      </div>
      <div>
        <div class="question">8. 请问您房产的大致价值范围？</div>
        <el-slider v-model="assetVal"></el-slider>
      </div>
      <div>
        <div class="question">9. 您大致的流动资产价值（包括现金、理财）</div>
        <el-slider v-model="flowAssetVal"></el-slider>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="submit" size="mini">提 交</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
export default {
  data () {
    return {
      list: [
        {
          id: '1',
          num: '0',
          name: '万笔',
          desc: '风险限额模块在工作日的日均调用量超过40万笔'
        },
        {
          id: '2',
          num: '00',
          name: '万客户',
          desc: '限额模块月均服务客户数量超600万'
        },
        {
          id: '3',
          num: '',
          name: '倍',
          desc: '超过风险限额的客户违约率是超过行内原有限额的3倍'
        }
      ],
      dialogVisible: false,
      anchorVal: 0,
      topVal: [0, 1],
      options: [{
        value: '选项1',
        label: '黄金糕'
      }, {
        value: '选项2',
        label: '双皮奶'
      }],
      selVal: '',
      menuList: [
        { id: 'challenge', name: '背景与挑战', flag: 'challengeFlag', slide: 2, page: 1 },
        { id: 'risk', name: '什么是风险限额', flag: 'riskFlag', slide: 3, page: 2 },
        { id: 'way', name: '我们的方法', flag: 'wayFlag', slide: 4, page: 3 },
        { id: 'video', name: '宣传片', flag: 'videoFlag', slide: 5, page: 4 },
        { id: 'bottom', name: '零售客户风险限额', flag: 'bottomFlag', slide: 6, page: 5 }
      ],
      addressVal: '',
      addOptions: [
        {
          value: '1',
          label: '北京',
          children: [
            {
              value: '2',
              label: '海淀'
            }
          ]
        }
      ],
      number: 0,
      incomeVal: 0,
      assetVal: 0,
      flowAssetVal: 0,
      challengeFlag: false,
      riskFlag: false,
      wayFlag: false,
      videoFlag: false,
      bottomFlag: false,
      numFlag: false, // 首页数字滚动
      fullOptions: {
        licenseKey: null,
        css3: true,
        scrollBar: true,
        navigation: false,
        // autoScrolling: false, // 设为false后，会出现浏览器自带的滚动条，将不会按页滚动
        navigationPosition: 'left',
        // navigationTooltips: ['背景与挑战', '什么是风险限额', '我们的方法', '宣传片', '零售客户风险限额'],
        afterLoad: this.afterLoad,
        duration: 500,
        onLeave: this.onLeave
      },
      numPage: 0
    }
  },
  computed: {
    setBorderColor () {
      return function () {
        if (this.numPage === 1 || this.numPage === 3 || this.numPage === 5) {
          return 'divider-odd'
        } else {
          return 'divider-even'
        }
      }
    },
    setMargin () {
      return function (val) {
        if (val === '2') {
          return 'customer-mar'
        } else if (val === '3') {
          return 'times-mar'
        } else if (val === '1') {
          return 'first-mar'
        }
      }
    }
  },
  mounted () {
    this.numFlag = true
    const demo = document.querySelector('.top')
    const length = document.querySelector('.top').offsetWidth / 2
    const background = document.querySelector('.back-img')
    demo.addEventListener('mousemove', function (e) {
      const x = (length - e.pageX) / 10
      background.style.transform = `translateX(${x}px)`
    })
  },
  methods: {
    question () {
      this.dialogVisible = true
      this.fullOptions.autoScrolling = false
      this.fullOptions.scrollBar = false
    },
    scrollEvent (e) {
      const flags = this.menuList.map(item => item.flag)
      // const id = '.' + e.id
      // const el = document.querySelector(id)
      this.$nextTick(function () {
        flags.map(ele => {
          if (ele === e.flag) {
            this[e.flag] = true
          } else {
            this[ele] = false
          }
        })
        // window.scrollTo({'behavior': 'smooth', 'top': el.offsetTop})
      })
      this.$refs.fullpage.api.moveTo(e.slide, 0)

      // this.$refs.fullpage.api.moveSectionDown()
      // this.$refs.fullpage.init()
      // this.$refs.fullpage.reBuild()
    },
    handleChange () {

    },
    selectBtn () {

    },
    changeVal (val) {
      this.number = val[val.length - 1]
    },
    afterLoad (origin, destination, direction) {
      // direction：向上或向下
      const el = document.querySelectorAll('.aside-text')
      // const divider = document.querySelectorAll('.divider-text')
      // const backImg = document.querySelector('.back-img')
      this.numFlag = destination.index === 0
      this.menuList.map(item => {
        if (item.page === destination.index) {
          this[item.flag] = true
        } else {
          this[item.flag] = false
        }
      })
      console.log(direction)
      // 设置字体颜色
      if (direction) {
        this.numPage = destination.index
        if (destination.index === 2 || destination.index === 4 || destination.index === 5) {
          for (let i = 0; i < el.length; i++) {
            el[i].style.color = '#fff'
          }
        } else {
          for (let i = 0; i < el.length; i++) {
            el[i].style.color = '#636363'
          }
        }
      }
    },
    onLeave () {

    },
    submit () {
      this.dialogVisible = false
      this.fullOptions.autoScrolling = true
      this.fullOptions.scrollBar = true
    }
  }
}
</script>
<style lang="less" scoped>
.contain {
  width: 100%;
  height: 100%;
  overflow-x: hidden;
  /deep/ .el-dialog__wrapper {
    overflow-y: hidden;
  }
  /deep/ .el-dialog {
    height: 700px;
    overflow-y: scroll;
  }
  .top {
    width: 100%;
    height: 100vh;
    /deep/ .fp-tableCell {
      display: flex;
      align-items: center;
      justify-content: center;
      flex-wrap: wrap;
    }
    .title {
      width: 100%;
      font-size: 60px;
      font-weight: 500;
      color: #fff;
      line-height: 84px;
      text-align: center;
    }
    .intro {
      width: 60%;
      margin-left: 20%;
      font-size: 36px;
      color: #fff;
      line-height: 56px;
      text-shadow: 3px 2px 6px rgba(0, 0, 0, 0.29);
      text-align: center;
      margin-top: 50px;
    }
    .desc {
      display: flex;
      margin-top: 120px;
      color: #fff;
      justify-content: center;
      .num-wrapper {
        overflow: hidden;
        font-size: 60px;
        position: relative;
        .first-mar {
          margin-left: 10px;
        }
        .customer-mar {
          margin-left: 42px;
        }
        .times-mar {
          margin: -30px;
        }
      }
      // ---
      .num_one {
        position: absolute;
        top: -603%;
        left: 0;
      }
      .num_one-enter-active {
        transition: all 2s ease;
        -webkit-transition: all 2s ease;
      }
      .num_one-leave-active {
        transition: all 1 ease;
        -webkit-transition: all 1 ease;
      }
      .num_one-enter, .num_one-leave-to {
        transform: translateY(54%);
        -webkit-transform: translateY(54%);
        opacity: 0;
      }
      // ---
      .num_two {
        position: absolute;
        top: -952%;
        left: 13%;
      }
      .num_two-enter-active {
        transition: all 3s ease;
        -webkit-transition: all 3s ease;
      }
      .num_two-leave-active {
        transition: all 2 ease;
        -webkit-transition: all 2 ease;
      }
      .num_two-enter, .num_two-leave-to {
        transform: translateY(54%);
        -webkit-transform: translateY(54%);
        opacity: 0;
      }
      // ---
      .num_three {
        position: absolute;
        top: -1128%;
        left: 26%;
      }
      .num_three-enter-active {
        transition: all 4s ease;
        -webkit-transition: all 4s ease;
      }
      .num_three-leave-active {
        transition: all 3 ease;
        -webkit-transition: all 3 ease;
      }
      .num_three-enter, .num_three-leave-to {
        transform: translateY(54%);
        -webkit-transform: translateY(54%);
        opacity: 0;
      }
      .name {
        font-size: 21px;
      }
      .text {
        width: 288px;
        font-size: 18px;
      }
    }
    .desc > div {
      border-right: 1px solid #fff;
      padding: 0 50px;
    }
    .desc > div:nth-last-child(1) {
      border: none;
    }
  }
  .fullpage-wrapper {
    .back-img {
      position: absolute;
      top: 0;
      left: -5%;
      width: 110%;
      height: 100vh;
      z-index: -1;
      background: url('../assets/domain.jpg') no-repeat;
      background-size: 100% 100%;
      background-position: center 0;
    }
  }
  .fullpage-wrapper:hover {
    .back-img {
      animation: animate 6s infinite;
    }
  }
  @keyframes animate {
    0% {
      background-size: 100% 100%;
    }
    50% {
      background-size: 100% 110%;
    }
  }
  .anchor {
    position: fixed;
    top: 5%;
    left: 3%;
    z-index: 99;
    span {
      display: inline-block;
      width: 48%;
      height: 50%;
      box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.3);
    }
    .aside {
      font-size: 14px;
      font-weight: 500;
      margin-top: 40px;
      div {
        height: 40px;
        line-height: 40px;
        margin-bottom: 2px;
        cursor: pointer;
        border-left: 1px solid rgb(158, 155, 155);
        line-height: 40px;
        padding-left: 10px;
      }
      .aside-text {
        opacity: 0;
        color: #636363;
        box-shadow: none;
      }
      .aside-text:hover {
        opacity: 1;
        color: #fff;
      }
      .divider-odd:hover {
        border-left-color: #000;
      }
      .divider-even:hover {
        border-left-color: #fff;
      }
    }
    .point-block {
      width: 50%;
      height: 50%;
      margin-top: 20px;
    }
  }
  .challenge {
    .bk-five {
      overflow: hidden;
      height: 100vh;
      .scaleBk {
        width: 190%;
        height: 150vh;
        background: url("../assets/bk_five.jpg") no-repeat;
        background-size: 100% 100%;
        background-position: center 0;
        position: relative;
        transform: translate(-30%, -25%) rotate(30deg);
      }
    }
    .fade-enter-active {
      transition: all 2s ease;
      -webkit-transition: all 2s ease;
    }
    .fade-leave-active {
      transition: all 0.3 ease;
      -webkit-transition: all 0.3 ease;
    }
    .fade-enter, .fade-leave-to {
      transform: translateY(50%);
      opacity: 0;
    }
  }
  .el-col-14 {
    height: 100vh;
    display: flex;
    // align-items: center;
    // justify-content: center;
    padding-top: 12%;
    padding-left: 14%;
  }
  .c-left {
    width: 90%;
    .title {
      font-size: 60px;
    }
    p {
      font-size: 18px;
      line-height: 24px;
      color: #787878;
    }
  }
  .risk {
    .el-col {
      height: 100vh;
    }
    .el-col-10 {
      background: url("../assets/bk_four.jpg") no-repeat;
      background-size: 100% 100%;
      background-position: center 0;
    }
    .el-col-14 {
      background: #23283c;
      color: #fff;
    }
    .fade-risk-enter-active {
      transition: all 2s ease;
      -webkit-transition: all 2s ease;
    }
    .fade-risk-leave-active {
      transition: all 0.3 ease;
      -webkit-transition: all 0.3 ease;
    }
    .fade-risk-enter, .fade-risk-leave-to {
      transform: translateY(50%);
      opacity: 0;
    }
  }
  .risk-content {
    position: relative;
  }
  .r-right {
    width: 90%;
    .title {
      font-size: 60px;
    }
    p {
      font-size: 18px;
      line-height: 24px;
      color: #787878;
    }
  }
  .way-content {
    position: relative;
  }
  .way {
    .el-col {
      height: 100vh;
      // height: 80vh;
    }
    .el-col-10 {
      background: url("../assets/bk_six.jpg") no-repeat;
      background-size: cover;
      background-position: center center;
    }
    .fade-way-enter-active {
      transition: all 2s ease;
      -webkit-transition: all 2s ease;
    }
    .fade-way-leave-active {
      transition: all 0.3 ease;
      -webkit-transition: all 0.3 ease;
    }
    .fade-way-enter, .fade-way-leave-to {
      transform: translateY(50%);
      opacity: 0;
    }
    .func {
      margin-top: 70px;
      width: 90%;
      height: 222px;
      background: url('../assets/flow_func.png') no-repeat;
      background-size: 100% 100%;
      background-position: center 0;
    }
  }
  .video {
    height: 100vh;
    background: #000;
    position: relative;
  }
  .bottom-content {
    position: relative;
    overflow-y: hidden;
  }
  .bottom {
    .el-col {
      height: 100vh;
    }
    .el-col-10 {
      background: url("../assets/bk_two.jpeg") no-repeat;
      background-size: 100% 100%;
      background-position: center 0;
    }
    .fade-bottom-enter-active {
      transition: all 2s ease;
      -webkit-transition: all 2s ease;
    }
    .fade-bottom-leave-active {
      transition: all 0.3 ease;
      -webkit-transition: all 0.3 ease;
    }
    .fade-bottom-enter, .fade-bottom-leave-to {
      transform: translateY(50%);
      opacity: 0;
    }
    /deep/ .fp-tableCell {
      overflow-y: hidden;
    }
  }
  .dialog-footer .el-button {
    border: 1px solid #1657d9;
    color: #1657d9;
  }
  .question {
    height: 50px;
    line-height: 50px;
    margin-top: 20px;
    font-size: 16px;
  }
  /deep/ .el-button--primary {
    color: #409eff;
    background: #fff;
  }
  .title-slider {
    /deep/ .el-slider__button {
      display: none;
    }
    /deep/ .el-slider__bar {
      background: #409EFF;
    }
    /deep/ .el-slider__button-wrapper:hover {
      cursor: default;
    }
    /deep/ .el-slider__button-wrapper {
      display: none;
    }
  }
  .modal {
    /deep/ .el-dialog__body {
      padding: 0 80px;
    }
  }
  .abstruct {
    width: 30px;
    height: 40px;
    position: absolute;
    bottom: 20px;
    right: 0;
  }
}
</style>

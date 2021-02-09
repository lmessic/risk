// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Router from 'vue-router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'fullpage.js/vendors/scrolloverflow'
import './fullpage.min.css'
import VueFullPage from 'vue-fullpage.js'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(Router)
Vue.use(VueFullPage)
router.afterEach((to, from, next) => {
  window.scrollTo(0, 0)
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

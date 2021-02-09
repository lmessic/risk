import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '*',
      redirect: '/risk'
    },
    {
      path: '/risk',
      name: '首页',
      component: () => import('@/views/index')
    },
    {
      path: '/detail',
      name: '详情',
      component: () => import('@/views/detail')
    }
  ]
})

// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// import Vue from 'todo/static/vue/dist/vue.min'
import Vue from '../static/vue/dist/vue.min'
// import Vue from 'vue/dist/vue.min';
x
import App from './App'

new Vue(App).$mount('.vue-root');

if (ENVIRONMENT === 'local') {
  Vue.config.devtools = true;
}

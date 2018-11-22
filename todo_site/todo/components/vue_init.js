import Vue from '../static/vue/dist/vue.min';
import App from '../components/App.vue';

new Vue(App).$mount('.vue-root');

if (ENVIRONMENT === 'local') {
  Vue.config.devtools = true;
}

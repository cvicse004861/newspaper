import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import VueAMap, {initAMapApiLoader} from '@vuemap/vue-amap';
import '@vuemap/vue-amap/dist/style.css'

const app = createApp(App)

initAMapApiLoader({
    key: 'aaf83fb9ea932541051f7ad132a6aac8',
    plugin: ''
})

app
    .use(ElementPlus)
    .use(VueAMap)
    .mount('#app')

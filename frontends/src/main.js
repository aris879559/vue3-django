import { createApp, provide } from 'vue'
import App from './App.vue'
// import './index.css'
import { backendUrl } from './config.js';

// createApp(App).mount('#app')
const app = createApp(App)

// 定义并提供 backend_url
// app.provide('backend_url', 'http://127.0.0.1:8080/api/lyb/')
app.provide('backend_url', backendUrl);

app.mount('#app')
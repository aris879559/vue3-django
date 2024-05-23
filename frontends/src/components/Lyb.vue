<template>
  <div class="row">
    <div class="col-md-8">
      <table class="table table-bordered">
        <thead>
          <tr>
            <th>标题</th>
            <th>作者</th>
            <th>内容</th>
            <th></th>
          </tr>
        </thead>
        <thead>
          <tr v-for="item in lyb_list" :key="item.url">
            <td>{{item.title}}</td>
            <td>{{item.author}}</td>
            <td>{{item.content}}</td>
            <td>
              <button class="btn btn-success" title="编辑" @click="editLyb(item)" style="margin: 0 10px;">
                <i class="glyphicon glyphicon-pencil"></i>
              </button>
              <button class="btn btn-danger" title="删除" @click="deleteLyb(item)">
                <i class="glyphicon glyphicon-trash"></i>
              </button>
            </td>
          </tr>
        </thead>
      </table>
    </div>
    <div class="col-md-4">
      <input type="hidden" v-model="lyb.url">
      <div class="form-group">
        <label for="title">标题:</label>
        <input type="text" id="title" class="form-control" v-model="lyb.title">
      </div>
      <div class="form-group">
        <label for="author">作者:</label>
        <input type="text" id="author" class="form-control" v-model="lyb.author">
      </div>
      <div class="form-group">
        <label for="content">内容:</label>
        <textarea id="content" cols="30" rows="10" class="form-control" v-model="lyb.content"></textarea>
      </div>
      <div class="form-group">
        <button class="btn btn-default" @click="saveLyb">确定</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { reactive, onMounted, toRefs, inject } from 'vue'
export default {
  name: 'Lyb',
  setup() {
    // 后台数据接口地址
    // let backend_url = "http://127.0.0.1:8080/api/lyb/";
    const backend_url = inject('backend_url');
    const lyb_obj = {
      url: '',
      title: '',
      author: '',
      content: '',
    }
    const state = reactive({
      // 获取数据指令
      lyb_list: [],
      // 获取单条数据
      lyb: Object.assign({}, lyb_obj),
    });
    const getLyb = () => {
      axios.get(backend_url).then(res => {
        // console.log(res);
        state.lyb_list = res.data;
        // 查询数据之后，清空数据
        state.lyb = Object.assign({}, lyb_obj);
      }).catch(err => {
        console.log(err);
      })
    };
    const editLyb = (item) => {
      state.lyb.url = item.url;
      state.lyb.title = item.title;
      state.lyb.author = item.author;
      state.lyb.content = item.content;
    };
    const saveLyb = () => {
      let newdata = {
        title: state.lyb.title,
        author: state.lyb.author,
        content: state.lyb.content,
      }
      if(state.lyb.url == "") {
          // 新增
          axios.post(backend_url, newdata).then(() => {
            getLyb();
          }).catch(err => {
            console.log(err);
          })
      } else {
        // 编辑
        axios.put(state.lyb.url, newdata).then(() => {
          getLyb();
        }).catch(err => {
          console.log(err);
        })
      }
    };
    const deleteLyb = (item) => {
      axios.delete(item.url).then(() => {
        getLyb();
      }).catch(err => {
        console.log(err);
      })
    }
    onMounted(() => {
      getLyb();
    });
    return { 
      ...toRefs(state),
      editLyb,
      saveLyb,
      deleteLyb,
      backend_url,
    };
  },
}
</script>

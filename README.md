# flask-vue

## Project setup
```
yarn install
# Or use npm
# npm install
```

### Compiles and hot-reloads for development
```
yarn serve
# npm run serve
```

### Compiles and minifies for production
```
yarn build
# npm run build
```

### Lints and fixes files
```
yarn lint
# npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## 启动步骤

开发环境，分别启动 flask & vue

```bash
python3 server.py
yarn serve # Or npm run serve
```

生产环境，先编译vue项目
```bash
yarn build # Or npm run build
```

再启动flask服务，vue打包后文件在/static文件夹下，由flask做静态服务（避免跨域）
```bash
python3 server.py
```
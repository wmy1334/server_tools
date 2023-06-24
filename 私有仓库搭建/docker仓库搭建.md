# docker私有仓库搭建

## 下载镜像
docker pull docker.io/registry

## 启动镜像
`docker run -d -p 5000:5000 -v /local_path:/var/lib/registry --restart=always --name=uosregistry docker.io/registry`


## 容器指定访问仓库
vim /etc/docker/daemon.json
```json
{
  "insecure-registries": [
    "192.168.122.49:5000"
  ]
}
```

`systemctl restart docker`

## 上传镜像到本地仓库

### 修改镜像tag
docker tag 
`docker push xxx/xxx`

## 测试
curl ip:5000/v2/_catalog
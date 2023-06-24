```commandline
yum install -y yum-utils createrepo

mkdir -p /data/repos

mkdir -p /data


createrepo /opt/repos

yum clean all
yum makecache

```

## yum repos 配置文件说明
vim local.repo
```commandline
[local] # 与创建的repo文件名相同，比如本文件为local.repo
name=test  # yum仓库名字
baseurl=file:///mnt  # 可本地，可远程
enabled=1 # 开启yum仓库
gpgcheck=0 # 不要检查序列号
```
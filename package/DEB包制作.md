# deb包制作

## 目录结构
DEBIAN文件夹中必须有control文件，表示安装包基本信息。（DEBIAN权限755）

除此之外，其中还可以有：

- preinst 软件安装之前会执行的脚本
- postinst 软件安装完成后执行的脚本
- prerm 软件卸载前会执行的脚本
- postrm 软件卸载后会执行的脚本


opt 存放软件

简单的命令行工具可直接创建/usr/bin目录并将程序移动该目录下


## 文件字段说明

### control

#### 必选和常用字段
- Package 包名（小写字母和-+字符）
- Version 版本号
- Section 软件的类别，可以是utils、net、mail、text、devel等等
- Priority 软件对于系统的重要程度，如required、standard、 optional、extra等等
- Architecture 架构，32位软件填写i386，64位软件填写amd64，如果是既能在32位系统运行又能在64为系统运行可以填写all
- Installed-Size 安装后大小，单位为kb
- Maintainer 维护者，为维护者名<邮箱>的形式
- Provides 供应者
- Description 描述
- Source 源代码名称，非必须，可以删去
- Homepage: 软件官网主页

#### 额外字段
- Essential 申明是否是系统最基本的软件包，值为yes或者no，如果是的话，这就表明该软件是维持系统稳定和正常运行的软件包，不允许任何形式的卸载
- Depends 软件所依赖的其他软件包和库。如果是依赖多个软件包，彼此之间采用英文逗号隔开（例如该值为libc6, default-jre，说明该软件包依赖于libc6- 和default-jre这两个软件包，缺一不可）
- Pre-Depends 软件安装前必须安装、配置依赖性的软件包和库
- Recommends 这个字段表明推荐的安装的其他软件包
- Suggests 建议安装的其他软件包

> 注意，control文件最末尾必须保留一个空行，否则打包会报错。

## 桌面快捷方式
保存为.desktop文件，并移动到/usr/share/applications目录下
```ini
[Desktop Entry]
Name=firefox
Name[zh_CN]=firefox-浏览器
Comment=visit the internet
Comment[zh_CN]=访问互联网
Version=1.0
Exec=/home/swsk33/应用/firefox/firefox
Path=/home/swsk33/应用/firefox
Icon=/home/swsk33/应用/firefox/firefox.png
Terminal=false
Type=Application
Categories=Network
StartupNotify=true
```

### 字段说明

- Name 应用名称
- Name[zh_CN] 应用在中文语言环境下显示的名称（可选）
- Commet 应用描述（可选）
- Commet[zh_CN] 应用在中文语言环境下显示的描述（可选）
- Version 版本号（可选）
- Exec 点击该图标后执行命令，一般填可执行文件的路径即可
- Path 应用程序（或者命令）的运行路径，一般填可执行文件所在文件夹（可选）
- Icon 应用图标，可以填图标图片位置，也可以是应用程序的可执行文件路径因为一些可执行文件自带图标（可选）
- Terminal 是否在终端打开，窗口应用程序一般填写false，命令行程序填true（可选）
- Type 类型，一般填Application
- StartupNotify 启动提示，一般可以填true（可选）
- Categories 应用范畴，可以写多个值，中间用分号隔开，详见下面类型表（可选）
  - Network	网络应用
  - Development	编程开发
  - Office	办公学习
  - AudioVideo	多媒体软件
  - Audio	音乐欣赏（该条目需要和AudioVideo同时存在）
  - Video	视频播放（该条目需要和AudioVideo同时存在）
  - Education	教育学习
  - Graphics	图形图像
  - Game	游戏娱乐
  - Viewer	阅读翻译
  - Settings	配置设置应用
  - Utility	实用工具
  - System	系统应用

## 打包

`dpkg -b "待打包目录" "生成deb安装包目录"`


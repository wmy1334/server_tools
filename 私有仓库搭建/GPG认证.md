## 安装
```commandline
sudo apt install gnupg
```

## 创建密钥对
```commandline
[fan 18:58:33]~$ gpg --gen-key
gpg (GnuPG) 1.4.20; Copyright (C) 2015 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

请选择您要使用的密钥种类：
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (仅用于签名)
   (4) RSA (仅用于签名)
您的选择？
RSA 密钥长度应在 1024 位与 4096 位之间。
您想要用多大的密钥尺寸？(2048) 4096
您所要求的密钥尺寸是 4096 位
请设定这把密钥的有效期限。
         0 = 密钥永不过期
      <n>  = 密钥在 n 天后过期
      <n>w = 密钥在 n 周后过期
      <n>m = 密钥在 n 月后过期
      <n>y = 密钥在 n 年后过期
密钥的有效期限是？(0)
密钥永远不会过期
以上正确吗？(y/n) y

您需要一个用户标识来辨识您的密钥；本软件会用真实姓名、注释和电子邮件地址组合
成用户标识，如下所示：
    "Heinrich Heine (Der Dichter) <heinrichh@duesseldorf.de>"

真实姓名： Fan
电子邮件地址： fan@qq.com
注释： github
您选定了这个用户标识：
    "Fan(github) <fan@qq.com>"

更改姓名(N)、注释(C)、电子邮件地址(E)或确定(O)/退出(Q)？ O
您需要一个密码来保护您的私钥。

我们需要生成大量的随机字节。这个时候您可以多做些琐事(像是敲打键盘、移动
鼠标、读写硬盘之类的)，这会让随机数字发生器有更好的机会获得足够的熵数。
....+++++

随机字节不够多。请再做一些其他的琐事，以使操作系统能搜集到更多的熵！
(还需要184字节)
+++++
我们需要生成大量的随机字节。这个时候您可以多做些琐事(像是敲打键盘、移动
鼠标、读写硬盘之类的)，这会让随机数字发生器有更好的机会获得足够的熵数。

随机字节不够多。请再做一些其他的琐事，以使操作系统能搜集到更多的熵！
(还需要231字节)
...+++++

随机字节不够多。请再做一些其他的琐事，以使操作系统能搜集到更多的熵！
(还需要170字节)
+++++
gpg: 密钥 2DBA87CF 被标记为绝对信任
公钥和私钥已经生成并经签名。

gpg: 正在检查信任度数据库
gpg: 需要 3 份勉强信任和 1 份完全信任，PGP 信任模型
gpg: 深度：0 有效性：  1 已签名：  0 信任度：0-，0q，0n，0m，0f，1u
pub   4096R/2DBA87CF 2017-04-11
      密钥指纹 = 3C00 AC7B 3D06 E22E AEDE  72B0 B28F ACA4 2EBC 87DF
uid                  Fan (github) <fan@qq.com>
sub   4096R/873278A9 2017-04-11

```

后续操作
```commandline
# 最好制作一张撤销证书，用于密钥作废，请求外部公钥服务器撤销你的公钥
# 这里 2DBA87CF 为我的 key id 
gpg --gen-revoke 2DBA87CF

# 上传公钥到公共的公钥服务器。
$ gpg --send-keys 2DBA87CF

# 任何人都可以用你的名义上传公钥所以我们可以
# 生成用于公布的公钥指纹，然后进行公布，比如我在文末公布了自己的公钥指纹，好让他人校验
$ gpg --fingerpint 2DBA87CF
密钥指纹 = 3C00 AC7B 3D06 E22E AEDE  72B0 B28F ACA4 2EBC 87DF
```

用户ID 就是 uid ，比如上面输出的 uid Fan (github) <fan@qq.com>

而这里的 2DBA87CF 应该称作为：

密钥ID
KEY_ID
或者更确切的说，它是 MASTERKEYID （主key id）。
> 另外还有 SUBKEYID。
用户邮箱 和 MASTERKEYID 在一些场合可以相互替换，但不是全部场合（被这个坑过）。

用户名和电子邮件。可以给同样的密钥不同的身份，比如给同一个密钥关联多个电子邮件。
任何导入密钥的人都可以看到这里的用户名和电子邮件地址。
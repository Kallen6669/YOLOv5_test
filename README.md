该项目是用于体验yolo系列的编程，分别由jittor和pytorch两个框架实现。

### 云服务器连接该项目的流程
1. 设置用户名和邮箱
```
git config --global user.name  ""
git config --global user.email  ""
```
2. 设置密钥
```
cd .root/
mkdir .ssh
cd .ssh/
vim yunfuwuqi
vim yunfuwuqi.pub
chmod 600 ~/.ssh/yunfuwuqi
vim config
```
config的内容：
```
Host github.com
  IdentityFile ~/.ssh/yunfuwuqi
```
验证：
```
ssh -T git@github.com
```
3. 拷贝代码
git clone https://github.com/Kallen6669/YOLOv5_test.git

4. 远程连接
git remote set-url origin git@github.com:Kallen6669/YOLOv5_test.git
git push origin main
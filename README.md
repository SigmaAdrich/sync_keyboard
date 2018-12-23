# sync_keyboard
## 功能
Synchronous operation of the keyboard and mouse  
同步操作多台电脑的键盘和鼠标，驱动级的键盘操作  
发出键盘指令的电脑为发送端，接收信号的电脑为接收端  
嗯，懂得人自然知道是用来干什么的。

##运行环境
python3.6以上  
windows启动测试模式
键盘为ps/2接口
安装相应的库

## 运行  
发送端:进入send目录，打开udp_cli.py，修改目标ip和端口为接收端的ip和端口  
接收端:进入accept目录，打开listen.py，修改接收端口和ip  
发送端 pyhton monitorkey.py  
接收端使用管理员模式启动窗口
接收端 python listen.py  

## 注意
接收端启动后将鼠标焦点移动到其他地方就可以了，以免当前焦点在命令行窗口，将接受的按键都输入到命令行窗口

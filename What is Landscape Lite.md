# Landscape Lite 中文版操作指南：
	
# Landscape 能做些什么：
	Landscape Lite 基于 NI Labview 写成。目前提供下载的为 LV2014 32bit 编译成的可执行文件。
	Landscape 是一款稳定高速的多功能数据采集软件。
	Landscape 自带的通讯程式可以和几乎全部主流仪器进行通讯。除此之外，Landscape Lite 还可以通过调用用户自定义 VI 的方式，实现更加复杂的操作。

# 基本操作篇：

# 利用 Landscape 开始第一条测量：
	1. 编写可用的仪器配置文件：
		用户可参考 Proto.ini 的格式编写仪器配置文件。仪器配置文件的参数如下：
		a. 用于读数的仪器配置：
			[仪器昵称（请不要重复，否则调用时只会调用第一个仪器配置）]
			Address = "仪器的 VISA 地址或网络通讯地址等"
			Read = "仪器读数指令（不可为空），否则不会被程序视为可用的读数配置"
			RName = "数据保存时的变量名称，若仪器返回多个变量，则用 & \ $ 将仪器名称分开"
			Buffer = TRUE/FALSE 代表仪器是否有较大的读取Buffer，若仪器只进行一次读数，也可以填TRUE
		b. 用于扫场的仪器配置：
			[仪器昵称（同一个昵称可以同时拥有扫场和读数两种功能）]
			Address = "仪器的 VISA 地址或网络通讯地址等"
			Scan = "扫场命令 \ 获取当前设定值命令"
			SName = "仪器设定值的存储名称"
			Limit = "+仪器上限\+仪器下限"，无所谓上下限顺序，数值前方要加正负号
			Ramp = "1mV"仪器设定时的最大步距
			Delay = "10ms"每次更改仪器设定值时的等待时间
	2. 编写测量步骤：
		a. 打开程序，在 Data Folder Path 中选择数据存储路径。在 Ini File Path 中选择配置文件路径，选好路径之后勾选 Lock Ini File。如果能够成功勾选，并且在 Scan Instruments 和 Read Instrument 两栏有正确的仪器显示，则说明导入成功。
		b. 双击 Work List 或者点按 Edit 按钮可以调出测量步骤编辑器。每一个步骤可分为四部分：
			i. Work List Information: 存储该步骤的描述，测量文件名，还有测量笔记。
			ii. Scan List：存储该步骤的扫场设定。
			iii. Read List: 存储该步骤的读数仪器。
			iiii. Array Type：存储该步骤的数列类型，以及每个参数的读点数目，读点时间间隔。
		c. 点按 Work List 旁边的四个按钮可以分别调出四部分的更改窗口。也可以通过右键菜单打开更改界面。

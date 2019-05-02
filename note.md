# GUI
- TKinter
    - 绑定的TK GUI工具集
- PyGTK
    - Tkinter的替代品
## TKinter常用组件 01.PY
- 按钮
    Button (command button的行为)
    RadioButton
    CheckButton
    Listbox
- 文本
    Entry
    Text
- 标签
    Label
    Message
- 菜单
    Menu
    MenuButton
- 滚动条
    scale
    Scrollbar
- 其他
    Canvas
    Frame
    Toplevel
## 组件的使用步骤
- 创建总面板
- 创建面板上的各种组件
    - 指定组件的父组件
    - 利用相应的属性对组件进行设置
    - 给组件安排布局
- 创建其他组件
- 启动总面板消息循环
##组件布局
- 三种布局
    - pack 按照方位布局 
    - place 按照坐标布局
    - grid 网格布局
- pack
    - 挨个放
    - 组件对象.pack(设置)
    - side：停靠方位  LEFT TOP RIGHT BOTTOM
    - fill:填充方式 X Y BOTH NONE
    - anchor :N E S W CENTER
    - expand: YES/NO
- grid
    - 组件对象.grid(设置)
    - 利用row column编号
- place
### 消息机制 02.py
- 消息的传递机制
    - 自动发出事件/消息
    - 相关组件进行绑定/设置
    - 后端自动选择感兴趣的事件作出相应反应
- 消息格式：
    - <[modifier-]---type-[-detail]>
    - <Button-1>:1 左键 2 中键
    - <KeyPress-A>:按下A
    - <Control-Shift-KeyPress-A>
- Tkinter的绑定
    - bind-all:全局范围的绑定
    - bind_class: 接收三个参数 类名 事件 操作
    - bind: 单独对一个实例绑定
    - unbind：解绑
###组件
- Entry 
    entry["show"]="*" 设置遮挡字符
- Menu
    - 第一个Menu类定义的是parent
    - add_command 添加菜单项
        顶层菜单从左向右添加 否则是下拉菜单 
        - label 菜单项名称
        - command 点击之后的命令
        - acceletor 快捷键
        - menu 属性指定 哪一个是顶级菜单
- 级联菜单
    - add_cascade:级联菜单 引出后面的菜单
    - menu 指定菜单级联到哪一个菜单上
    - 过程：
        - 建立menu实例
        - add_command
        - add_cascade
- 弹出式菜单
    - 过程
        - 建立菜单 向菜单添加各种功能
        - 监听鼠标右键
        - 根据位置弹出
        - 调用Menu的pop方法
- canvas画布
    - 画图
    - 
    

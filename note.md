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
### 消息机制
- 

    

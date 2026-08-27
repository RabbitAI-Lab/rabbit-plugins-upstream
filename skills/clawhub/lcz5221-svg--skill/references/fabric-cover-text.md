# Fabric.js 封面文字注入方法（核心难点）

封面是 Fabric.js 画布，文字是画布对象。**模拟 JS 双击(isTrusted=false)无法进入编辑态**，必须用 CDP 真实事件。

## 关键原理
Fabric.js 在文字进入编辑态时，会创建一个**隐藏的 textarea** 来接收键盘输入。绕过 UI 模拟，直接往这个隐藏 textarea 注入文字，最可靠。

## 操作步骤

### 1. 准备干净文字框
- 先清掉模板文字，恢复干净背景图
- 点「添加文字」生成干净文字框（显示「请输入文字」占位）

### 2. 用 CDP 真实双击进入编辑态
```bash
openclaw browser click-coords <x> <y> --double
```
- `<x> <y>` 是文字框中心屏幕坐标
- `--double` 走 CDP，isTrusted=true，才能被 Fabric 识别为双击

### 3. 定位文字中心（像素扫描）
用 evaluate 扫描画布找文字像素包围盒，换算屏幕坐标：
```js
const canvas = document.querySelectorAll('canvas.lower-canvas')[0];
const r = canvas.getBoundingClientRect();
// 扫描黄色/亮色文字像素，求包围盒[minX,minY,maxX,maxY]
// 屏幕坐标 = r.x + (minX+maxX)/4 , r.y + (minY+maxY)/4   (÷4 是因为DPR=2)
```

### 4. 注入文字到隐藏 textarea
检测并写入：
```js
const t = document.querySelector('textarea');
const setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
setter.call(t, '目标文字');
t.dispatchEvent(new Event('input', {bubbles:true}));
```

## 判断是否进入编辑态
- 出现**隐藏 textarea**（value 是被编辑文字）= 已进入编辑态
- 画布出现**蓝色选中框**像素 = 文字被选中
- 白色竖线 = 光标

## 踩坑
- 点封面「不使用」会连背景图一起清掉，需重传图片
- 误套系统模板产生「今日热点/全知道/救星」模板组，干扰定位
- 模拟鼠标双击(JS MouseEvent)无法进入 Fabric 编辑态，必须用 CDP(--double)
- canvas 物理像素 = 屏幕 × DPR(常为2)，换算要÷2

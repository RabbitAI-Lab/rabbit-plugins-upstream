---
name: android-control
description: "Android设备远程控制与屏幕理解引擎，基于uiautomator2+FastMCP，支持多设备连接池+心跳检测、UI层级解析(dump_hierarchy核心)、元素查找与点击、触控操作(点击/滑动/输入)、APP启停、消息收发、微信专用操作、AutoGLM视觉分析。触发: Android设备操作/微信自动化/屏幕理解/UI自动化/多设备管理"
tools: [read, write, memory_search]
dependencies: []
metadata:
  priority: P0
  category: device-ops
  openclaw:
    emoji: "⚙️"
    os: ["win32", "linux", "darwin"]
    requires:
      bins: ["python"]
      env: ["ANDROID_CONFIG_FILE"]
      config: ["mcp.servers.android-control-mcp"]
---

# Android设备远程控制与屏幕理解引擎

基于uiautomator2的多设备连接池管理，UI层级解析为核心屏幕理解方式，微信专用操作，AutoGLM视觉分析集成。

## 使用场景

1. 闲鱼App自动化操作（发布/擦亮/管理商品）
2. 微信消息自动收发（客服/通知/社群运营）
3. 多Android设备批量管理（连接池+心跳检测）
4. 移动端UI自动化测试
5. 屏幕内容理解与元素定位（dump_hierarchy核心）
6. APP启停与生命周期管理
7. 批量账号操作（多设备并行）
8. AutoGLM AI视觉分析（复杂界面理解）
9. 电商App批量操作与数据采集

## 工作流

### 主流程: 设备连接与管理

1. 调用connect_device连接目标设备（参数: device_id设备ID）
2. 执行业务操作
3. 操作完成后调用disconnect_device断开设备（参数: device_id设备ID）

### 主流程: 屏幕理解与元素操作（核心）

1. 调用dump_hierarchy获取UI层级结构（参数: device_id设备ID），用于理解当前界面布局
2. 调用find_element查找目标元素（参数: device_id, by查找方式resource_id/text/text_contains, value查找值）
3. 调用click_element直接点击目标元素（参数: by查找方式resource_id/text/text_contains, value查找值）
4. 如需坐标操作，调用tap点击屏幕指定坐标（参数: x X坐标, y Y坐标）
5. 调用take_screenshot截取当前屏幕（参数: device_id设备ID），用于视觉分析或记录

### 主流程: 触控操作

1. 调用tap点击屏幕坐标（参数: device_id, x, y）
2. 调用swipe滑动屏幕（参数: device_id, start_x起始X, start_y起始Y, end_x结束X, end_y结束Y, duration滑动时长秒默认0.5）
3. 调用input_text输入文本（参数: device_id, text文本内容，需先聚焦输入框）

### 主流程: APP操作

1. 调用start_app启动APP（参数: device_id, package_name包名如com.tencent.mm）
2. 执行APP内操作
3. 调用stop_app停止APP（参数: device_id, package_name包名）

### 主流程: 消息收发

1. 调用send_message发送消息（参数: device_id, app APP名称wechat/momo/soul, contact联系人, text消息内容）
2. 调用read_messages读取消息（参数: device_id, app APP名称, contact联系人, limit消息条数默认20）
3. 微信专用: 调用wechat_read_messages读取微信消息（参数: device_id, contact_name联系人名称, limit消息条数默认20）

### 主流程: 微信专用操作

1. 调用wechat_send_message发送微信消息（参数: device_id, contact_name联系人名称, message消息内容，基于规则实现）
2. 调用wechat_read_messages读取微信消息（参数: device_id, contact_name联系人名称, limit消息条数默认20）

### 主流程: AutoGLM视觉分析

1. 调用take_screenshot截取当前屏幕（参数: device_id设备ID）
2. 调用autoglm_analyze使用AutoGLM分析界面（参数: device_id, task_description任务描述，自动获取截图并准备数据供AutoGLM MCP进行智能分析）

### 主流程: 复杂业务编排（闲鱼发布示例）

1. connect_device连接目标设备
2. start_app启动闲鱼APP（package_name: com.taobao.idlefish）
3. click_element点击发布按钮（by: "text", value: "发布"）
4. input_text输入商品标题
5. 依次填写价格/描述/上传图片
6. click_element点击"确认发布"
7. stop_app关闭闲鱼APP
8. disconnect_device断开设备

## 输入格式

### 设备连接

```json
{
  "device_id": "android_001"
}
```

### 元素查找与点击

```json
{
  "device_id": "android_001",
  "by": "resource_id",
  "value": "com.taobao.idlefish:id/publish_button"
}
```

### 微信发消息

```json
{
  "device_id": "android_001",
  "contact_name": "张三",
  "message": "你好，请问有什么可以帮您？"
}
```

### 滑动操作

```json
{
  "device_id": "android_001",
  "start_x": 540,
  "start_y": 1800,
  "end_x": 540,
  "end_y": 400,
  "duration": 0.5
}
```

### AutoGLM分析

```json
{
  "device_id": "android_001",
  "task_description": "分析闲鱼商品发布页面的表单元素"
}
```

## 输出格式

### 操作结果输出

```json
{
  "success": true,
  "device_id": "android_001",
  "action": "click_element",
  "by": "text",
  "value": "发布",
  "timestamp": "2026-05-14T10:30:00"
}
```

### 微信消息输出

```json
{
  "success": true,
  "device_id": "android_001",
  "contact_name": "张三",
  "message": "你好，请问有什么可以帮您？",
  "sent_time": "2026-05-14T10:30:00"
}
```

## 异常处理

| 异常场景 | 错误代码 | 处理方式 | 恢复策略 |
|:---------|:---------|:---------|:---------|
| 设备未找到 | DEVICE_NOT_FOUND | 确认device_id正确，检查设备配置文件 | 重新连接或更换设备ID |
| 设备连接失败 | DEVICE_CONNECT_FAILED | 检查设备IP和ADB连接状态 | 重试3次，间隔5秒 |
| 设备离线 | DEVICE_OFFLINE | 检查心跳检测日志 | 重启ADB服务后重连 |
| 元素未找到 | ELEMENT_NOT_FOUND | click_element未找到目标元素 | 检查by/value参数，尝试text_contains模糊匹配 |
| 元素不可点击 | ELEMENT_NOT_CLICKABLE | 确认元素clickable属性为true | 改用tap坐标点击 |
| APP启动失败 | APP_START_FAILED | 确认package_name正确且APP已安装 | 检查设备已安装APP列表 |
| 输入文本失败 | INPUT_TEXT_FAILED | 确认输入框已聚焦 | 先click_element聚焦输入框再input_text |
| 微信联系人未找到 | CONTACT_NOT_FOUND | 确认联系人名称准确 | 使用autoglm_analyze视觉查找 |
| 消息发送失败 | MESSAGE_SEND_FAILED | 检查APP是否在前台 | 重新start_app后重试 |
| AutoGLM分析失败 | AUTOGLM_ANALYSIS_FAILED | 检查设备连接状态 | 降级为click_element规则模式 |
| MCP适配器未初始化 | ADAPTER_NOT_INITIALIZED | 等待自动初始化完成 | 检查devices.yaml配置文件 |
| 配置文件不存在 | CONFIG_FILE_MISSING | 检查ANDROID_CONFIG_FILE环境变量 | 创建默认devices.yaml配置 |

## 示例

### 示例1: 微信自动回复客户消息

```
设备: android_001
客户: 买家李四
消息: 您好，请问这个商品还有吗？
```

执行:
1. wechat_send_message回复（device_id: "android_001", contact_name: "买家李四", message: "亲，商品还有的，拍下马上发货~"）

输出:
```json
{
  "success": true,
  "device_id": "android_001",
  "contact_name": "买家李四",
  "message": "亲，商品还有的，拍下马上发货~",
  "sent_time": "2026-05-14T10:30:00"
}
```

### 示例2: 闲鱼商品发布自动化

```
设备: android_001
商品: AI绘画教程
价格: 9.9
```

执行:
1. connect_device连接android_001
2. start_app启动闲鱼（package_name: "com.taobao.idlefish"）
3. click_element点击发布（by: "text", value: "发布"）
4. input_text输入标题"AI绘画教程"
5. input_text输入价格"9.9"
6. click_element点击确认发布（by: "text_contains", value: "确认"）

输出:
```json
{
  "success": true,
  "device_id": "android_001",
  "action": "xianyu_publish",
  "product_title": "AI绘画教程",
  "price": "9.9",
  "published_at": "2026-05-14T10:35:00"
}
```

### 示例3: AutoGLM分析设备界面

```
任务: 分析某设备当前界面
```

执行:
1. autoglm_analyze分析界面（device_id: "android_001", task_description: "识别当前页面类型和可操作元素"）

输出:
```json
{
  "success": true,
  "devices": [
    {"device_id": "android_001", "status": "online", "current_app": "com.taobao.idlefish"},
    {"device_id": "android_002", "status": "offline"}
  ],
  "analysis": {
    "page_type": "商品详情页",
    "interactive_elements": ["立即购买", "联系卖家", "收藏"],
    "confidence": 0.89
  }
}
```

## 变更历史

| 版本 | 日期 | 变更内容 |
|:-----|:-----|:---------|
| v1.0 | 2026-05-14 | 初始版本，覆盖设备管理/屏幕理解/触控操作/APP操作/消息收发/微信专用/AutoGLM集成 |

---
slug: "amap-jsapi-skill"
name: "amap-jsapi-skill"
version: 1.1.2
displayName: "Amap Jsapi Skill"
summary: "高德地图 JSAPI v2.0 (WebGL) 开发技能。涵盖地图生命周期管理、强制安全配置、3D 视图控制、覆盖物绘制及 LBS 服务集成。"
license: "Proprietary"
description: |-
  高德地图 JSAPI v2。0 (WebGL) 开发技能。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API.
tags:
  - Security
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# Amap Jsapi Skill

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Amap Jsapi Skill涵盖地图生命周期管理 | 不支持 | 支持 |
| Amap Jsapi Skill强制安全配置 | 不支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |

## 核心能力

- 高德地图 JSAPI v2
- 0 (WebGL) 开发技能
- 涵盖地图生命周期管理、强制安全配置、3D 视图控制、覆盖物绘制及 LBS 服务集成
- \n\
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 地图初始化 | Web端Key与容器ID | 地图实例与控件状态 |
| 覆盖物绘制 | 坐标与样式参数 | Marker与Polygon对象 |
| 路径规划 | 起终点坐标 | 驾车与步行路线方案 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### 1. 引入加载器

使用 script 标签加载 loader.js：

```bash
<script src="https://webapi.amap.com/loader.js"></script>
```

### 2. 安全密钥配置 (强制)

**重要**：自 v2.0 起，必须在加载地图前配置安全密钥，否则无法通过鉴权。详情及后端代理示例请参考 [安全策略](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fsecurity.md&ownerHandle=lbs-amap).
> **安全提示**：安全密钥属于敏感凭据，请通过环境变量 `AMAP_SECURITY_JS_CODE` 传入，禁止在代码中硬编码。生产环境务必使用 `serviceHost` 代理方式，避免前端暴露密钥.
```javascript
// 在调用 AMapLoader.load 前执行
window._AMapSecurityConfig = {
  securityJsCode: process.env.AMAP_SECURITY_JS_CODE, // 通过环境变量安全获取
  // serviceHost: 'https://your-proxy-domain/_AMapService', // 生产环境：建议使用代理转发
};
```

### 3. 初始化地图

```javascript
import AMapLoader from '@amap/amap-jsapi-loader';
AMapLoader.load({
    key: '您的Web端开发者Key', // 必填
    version: "2.0",           // 指定版本
    plugins: ['AMap.Scale', 'AMap.ToolBar'] // 预加载插件
}).then((AMap) => {
    // 可选：设置应用标识，用于 API 调用来源统计
    AMap.getConfig().appname = 'amap-jsapi-skill';
// ...
    const map = new AMap.Map('container', {
        viewMode: '3D',       // 开启3D视图
        zoom: 11,             // 初始缩放级别
        center: [116.39, 39.90] // 初始中心点
    });
    map.addControl(new AMap.Scale());
}).catch(e => console.error(e));
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | amap-jsapi-skill处理的内容输入 |,  |
| content | string | 否 | amap-jsapi-skill处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "skill 相关配置参数",
    result: "skill 相关配置参数",
    result: "skill 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### 地图控制

* **生命周期**：`references/map-init.md` - 掌握 `load`、`Map` 实例创建及 `destroy` 销毁流程.
* **视图交互**：`references/view-control.md` - 控制 `zoom` (缩放)、`center` (平移)、`pitch` (俯仰)、`rotation` (旋转).
### 覆盖物绘制

* **点标记**：`references/marker.md` - 使用 `Marker` (基础)、`LabelMarker` (海量避让) 标注位置.
* **矢量图形**：`references/vector-graphics.md` - 绘制 `Polyline` (轨迹、线)、`Polygon` (区域、面)、`Circle` (范围、圆).
* **信息展示**：`references/info-window.md` - 通过 `InfoWindow` 展示详细信息.
* **右键菜单**：`references/context-menu.md` - 自定义地图或覆盖物的右键交互.
### 图层管理

* **基础图层**：`references/layers.md` - 标准、卫星、路网及 3D 楼块图层.
* **自有数据**：`references/custom-layers.md` - 集成 `Canvas`、`WMS/WMTS`, `GLCustomLayer` 地图上叠加 Canvas、WMS图层、 Threejs图层.
### 服务与插件

* **LBS 服务**：
  + `references/geocoder.md` - 地理编码/逆地理编码（地址/坐标互转）.
  + `references/routing.md` - 路径规划（驾车/步行/公交）.
  + `references/search.md` - POI 搜索与输入提示.
* **事件系统**：`references/events.md` - 响应点击、拖拽、缩放等交互事件.
## 常见问题

### Q1: 如何开始使用Amap Jsapi Skill？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用

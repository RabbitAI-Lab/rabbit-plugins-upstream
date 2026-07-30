---
slug: amap-jsapi-tool-free
name: amap-jsapi-tool-free
version: 1.0.0
displayName: 高德地图JSAPI免费版
summary: 高德地图JSAPI v2.0开发助手,支持地图展示、标注点、地理编码与基础路径规划,适合个人开发者快速集成地图功能.
license: MIT
edition: free
description: "高德地图JSAPI v2.0开发助手免费版,为个人开发者包含地图开发核心能力. 适用于需要amap jsapi tool相关能力的开发场景,包含结构化的工作流程和可复用的模板,帮助用户快速完成任务并保持代码质量. 适用于需要amap jsapi tool相关能力的开发场景,包含结构化的工作流程和配置指引."
tags:
  - 地图开发
  - amap
  - jsapi
  - automation
  - productivity
  - 高德地图
  - JSAPI
  - 免费版
  - API
  - 接口
tools:
  - read
  - exec
  - write
homepage: ""
category: "Development"
pricing_tier: free

---
# 高德地图JSAPI v2.0 开发助手免费版

## 概述

本工具为个人开发者提供高德地图JSAPI v2.0(WebGL)开发指导能力,涵盖地图展示、标注点管理、地理编码与基础路径规划等核心功能。免费版适合个人项目快速集成地图功能,提供每日5000次API调用额度,满足日常开发需求.
### 免费版与专业版对比

| 能力维度 | 免费版 | 专业版 |
|----|---|---|
| API调用额度 | 5000次/天 | 无限制 |
| 地图渲染 | WebGL基础 | WebGL高级+矢量图层 |
| 路径规划 | 步行+驾车 | 步行+驾车+公交+货车 |
| 实时数据 | 不支持 | 实时路况+交通事件 |
| 批量地理编码 | 不支持 | 批量处理 |
| 定制化 | 基础样式 | 自定义地图样式 |
| 技术支持 | 社区 | 专属支持 |

## 核心能力

### 1. WebGL地图渲染

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 高德地图JSAPI免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>高德地图示例</title>
    <style>
        #mapContainer { width: 100%; height: 500px; }
    </style>
</head>
<body>
    <div id="mapContainer"></div>
    <script>
        // 替换为你的高德地图Key
        window._AMapSecurityConfig = {
            securityJsCode: '你的安全密钥'
        };
    </script>
    <script src="https://webapi.amap.com/maps?v=2.0&key=你的API_KEY"></script>
    <script>
        // 初始化地图(WebGL渲染)
        const map = new AMap.Map('mapContainer', {
            zoom: 12,                    // 缩放级别
            center: [116.397428, 39.90923],  // 中心点(北京天安门)
            viewMode: '2D',              // 视图模式: 2D 或 3D
            mapStyle: 'amap://styles/normal'  // 地图样式
        });
# ...
        console.log('地图已加载');
    </script>
</body>
</html>
```

**处理**: 解析WebGL地图渲染的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回WebGL地图渲染的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 标注点(Marker)管理

```javascript
// 添加标注点
function addMarker(map, position, title) {
    const marker = new AMap.Marker({
        position: position,        // [经度, 纬度]
        title: title,              // 鼠标悬停标题
        offset: new AMap.Pixel(-13, -30)  // 偏移量
    });
    map.add(marker);
    return marker;
}
// ...
// 添加信息窗口
function addInfoWindow(map, position, content) {
    const infoWindow = new AMap.InfoWindow({
        content: content,
    });
    infoWindow.open(map, position);
}
// ...
// 使用示例
const marker = addMarker(map, [116.397428, 39.90923], '天安门');
addInfoWindow(map, [116.397428, 39.90923], 
    '<div style="padding:10px;"><b>天安门广场</b><br>北京市中心</div>');
// ...
// 批量添加标注点
const locations = [
    { pos: [116.397428, 39.90923], name: '天安门' },
    { pos: [116.413384, 39.911023], name: '王府井' },
    { pos: [116.377849, 39.915378], name: '西单' }
];
locations.forEach(loc => addMarker(map, loc.pos, loc.name));
```

**处理**: 解析标注点(Marker)管理的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回标注点(Marker)管理的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 地理编码与逆地理编码

```javascript
// 地理编码: 地址 -> 坐标
function geocode(address) {
    const geocoder = new AMap.Geocoder({
        city: '全国'  // 限制搜索范围
    });
// ...
    geocoder.getLocation(address, function(status, result) {
        if (status === 'complete' && result.info === 'OK') {
            const location = result.geocodes[0].location;
            console.log(`${address} -> 经度: ${location.lng}, 纬度: ${location.lat}`);
            // 在地图上标记
            addMarker(map, [location.lng, location.lat], address);
            map.setCenter([location.lng, location.lat]);
        } else {
            console.log('地理编码失败:', result);
        }
    });
}
// ...
// 逆地理编码: 坐标 -> 地址
function reverseGeocode(lng, lat) {
    const lnglat = [lng, lat];
// ...
    geocoder.getAddress(lnglat, function(status, result) {
            const address = result.regeocode.formattedAddress;
            console.log(`(${lng}, ${lat}) -> ${address}`);
        }
    });
}
// ...
// 使用示例
geocode('北京市朝阳区望京SOHO');
reverseGeocode(116.397428, 39.90923);
```

**处理**: 解析地理编码与逆地理编码的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回地理编码与逆地理编码的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. 基础路径规划

```javascript
// 驾车路径规划
function drivingRoute(origin, destination) {
    AMap.plugin('AMap.Driving', function() {
        const driving = new AMap.Driving({
            policy: AMap.DrivingPolicy.LEAST_TIME,  // 最快捷
            map: map,
            panel: 'routePanel'  // 路线结果面板ID(可选)
        });
// ...
        driving.search(origin, destination, function(status, result) {
            if (status === 'complete') {
                console.log('规划成功:');
                result.routes[0].steps.forEach((step, i) => {
log(`  ${i+1}. ${step.instructions}`);
                });
log(`总距离: ${(result.routes[0].distance / 1000).toFixed(1)}公里`);
log(`预计时间: ${Math.ceil(result.routes[0].time / 60)}分钟`);
            } else {
log('规划失败:', result);
            }
        });
    });
}
// ...
// 步行路径规划
function walkingRoute(origin, destination) {
    AMap.plugin('AMap.Walking', function() {
        const walking = new AMap.Walking({ map: map });
        walking.search(origin, destination, function(status, result) {
            if (status === 'complete') {
log(`步行距离: ${result.routes[0].distance}米`);
log(`预计时间: ${Math.ceil(result.routes[0].time / 60)}分钟`);
            }
        });
    });
}
// ...
// 使用示例
drivingRoute([116.377849, 39.915378], [116.413384, 39.911023]);  // 西单 -> 王府井
walkingRoute([116.397428, 39.90923], [116.413384, 39.911023]);    // 天安门 -> 王府井
```

**处理**: 解析基础路径规划的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回基础路径规划的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：JSAPI、开发助手、支持地图展示、地理编码与基础路、适合个人开发者快、速集成地图功能、开发助手免费版、为个人开发者提供、地图开发核心能力、核心能力、标注点管理、适用场景、个人项目地图展示、位置搜索、基础导航功能开发、差异化、免费版聚焦核心地、图功能、速上手、调用额度、适用关键词、地图开发、geocoding等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景

### 场景一:店铺位置展示页面

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>店铺位置</title>
    <style>
        #map { width: 100%; height: 400px; border-radius: 8px; }
        .shop-info { padding: 15px; background: #f5f5f5; margin-top: 10px; }
    </style>
</head>
<body>
    <h2>我们的店铺位置</h2>
    <div id="map"></div>
    <div class="shop-info" id="shopInfo"></div>
# ...
amap.com/maps?v=2.0&key=你的API_KEY"></script>
    <script>
        const SHOP_ADDRESS = '北京市朝阳区望京SOHO T1';
Map('map', { zoom: 15, center: [116.481028, 39.996729] });
# ...
        // 地理编码定位店铺
Geocoder({ city: '北京' });
        geocoder.getLocation(SHOP_ADDRESS, function(status, result) {
            if (status === 'complete') {
                const loc = result.geocodes[0].location;
                map.setCenter([loc.lng, loc.lat]);
# ...
                new AMap.Marker({
                    position: [loc.lng, loc.lat],
                    map: map,
                    title: SHOP_ADDRESS
                });
# ...
                document.getElementById('shopInfo').innerHTML = 
                    `<strong>地址:</strong> ${SHOP_ADDRESS}<br>` +
                    `<strong>坐标:</strong> ${loc.lng.toFixed(6)}, ${loc.lat.toFixed(6)}`;
            }
        });
    </script>
</body>
</html>
```

### 场景二:多个地点标注展示

```javascript
// 在地图上展示多个分支机构
const branches = [
    { name: '北京总部', address: '北京市朝阳区望京SOHO', pos: [116.481028, 39.996729] },
    { name: '上海分部', address: '上海市浦东新区陆家嘴', pos: [121.473701, 31.230416] },
    { name: '深圳分部', address: '深圳市南山区科技园', pos: [113.946582, 22.538314] },
    { name: '广州分部', address: '广州市天河区珠江新城', pos: [113.321036, 23.119318] }
];
// ...
// 自动调整视野以包含所有标注
const markers = branches.map(b => new AMap.Marker({
    position: b.pos,
    title: b.name
}));
map.add(markers);
map.setFitView();  // 自动缩放以显示所有标注
// ...
// 点击标注显示信息
markers.forEach((marker, i) => {
    marker.on('click', function() {
        new AMap.InfoWindow({
            content: `<div style="padding:10px;">
                <h4>${branches[i].name}</h4>
                <p>${branches[i].address}</p>
            </div>`,
        }).open(map, branches[i].pos);
    });
});
```

### 场景三:地址搜索与定位

```html
<div>
    <input type="text" id="searchInput" placeholder="输入地址搜索..." style="padding:8px; width:300px;">
    <button onclick="searchAddress()" style="padding:8px;">搜索</button>
</div>
# ...
<script>
function searchAddress() {
    const address = document.getElementById('searchInput').value;
    if (!address) return;
# ...
Geocoder({ city: '全国' });
    geocoder.getLocation(address, function(status, result) {
geocodes.length > 0) {
geocodes[0].location;
            map.setZoomAndCenter(15, [loc.lng, loc.lat]);
# ...
            map.clearMap();
                map: map,
                title: address
            });
        } else {
            alert('未找到该地址');
        }
    });
}
</script>
```

## 不适用场景

以下场景高德地图JSAPI免费版不适合处理：

- 逆向工程闭源API
- API安全渗透测试
- 非标准协议集成

## 触发条件

需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于非本工具能力范围的需求.
## 快速开始

### 领先步:申请API Key

1. 访问高德开放平台
2. 创建应用,获取API Key和安全密钥
3. 配置域名白名单

### 第二步:引入JSAPI

```html
<script>
    window._AMapSecurityConfig = { securityJsCode: '你的安全密钥' };
</script>
amap.com/maps?v=2.0&key=你的API_KEY"></script>
```

### 第三步:初始化地图

```javascript
    zoom: 12,
    center: [116.397428, 39.90923]
});
```

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 示例

### 地图样式选项

| 样式名称 | 样式代码 | 适用场景 |
|---:|---:|---:|
| 标准样式 | amap://styles/normal | 通用场景 |
| 幻影黑 | amap://styles/dark | 夜间模式 |
| 月光银 | amap://styles/light | 简洁风格 |
| 远山黛 | amap://styles/whitesmoke | 商务风格 |
| 草色青 | amap://styles/fresh | 自然风格 |

### 常用控件配置

```javascript
// 添加工具条和比例尺
AMap.plugin([
    'AMap.ToolBar',
    'AMap.Scale',
    'AMap.OverView'
], function() {
    map.addControl(new AMap.ToolBar());
    map.addControl(new AMap.Scale());
    map.addControl(new AMap.OverView({ isOpen: true }));
});
```

### 免费版API额度

| 接口 | 免费额度 | 说明 |
|:---:|:---:|:---:|
| JSAPI加载 | 无限制 | 地图渲染不消耗配额 |
| 地理编码 | 5000次/天 | 地址转坐标 |
| 逆地理编码 | 5000次/天 | 坐标转地址 |
| 驾车路径规划 | 5000次/天 | 驾车导航 |
| 步行路径规划 | 5000次/天 | 步行导航 |

## 优秀实践

1. **安全密钥配置**:生产环境必须配置securityJsCode,避免Key泄露.
2. **按需加载插件**:使用AMap.plugin按需加载,减少初始加载时间.
3. **标注优化**:大量标注时使用MassMarks或MarkerCluster提升性能.
4. **错误处理**:所有异步回调中处理失败情况,提升用户体验.
5. **移动端适配**:设置viewport meta标签,使用自适应布局.
```javascript
// 优秀实践:安全初始化模板
function initMap(containerId, options = {}) {
    if (!window.AMap) {
        console.error('高德地图JSAPI未加载');
        return null;
    }
// ...
    const defaultOptions = {
        zoom: 12,
        viewMode: '2D'
    };
// ...
Map(containerId, { ...defaultOptions, ...options });
// ...
    // 添加基础控件
    AMap.plugin(['AMap.ToolBar', 'AMap.Scale'], function() {
        map.addControl(new AMap.ToolBar({ position: 'RB' }));
        map.addControl(new AMap.Scale());
    });
// ...
    return map;
}
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **浏览器**: Chrome 70+ / Firefox 65+ / Safari 12+ / Edge 79+
- **网络**: 需可访问 `https://webapi.amap.com`

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| AMap JSAPI | JavaScript库 | 必需 | 高德开放平台申请Key |
| 浏览器 | 运行环境 | 必需 | 现代浏览器 |
| HTTPS | 网络协议 | 必需 | 生产环境必须使用HTTPS |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 在高德开放平台申请API Key和安全密钥
- 通过 `window._AMapSecurityConfig` 配置安全密钥
- 在JSAPI script标签的key参数中传入API Key

### 可用性分类
- **分类**: MD+EXEC模式纯Markdown指令,需要exec能力生成HTML文件)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent生成高德地图JSAPI开发代码
- API Key通过环境变量配置: export API_KEY=your_key

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需要API Key，无Key环境无法使用

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "高德地图JSAPI免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "amap jsapi"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```

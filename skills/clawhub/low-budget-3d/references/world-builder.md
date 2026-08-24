# World Builder - 世界构建器

## 场景建模

背景必须和角色一样粗糙。不能出现"粗糙角色 + 高级电影背景"。整个世界都要像同一个低成本动画团队制作。

场景使用：
- 简单山体
- 简单地面
- 低模树木
- 几何岩石
- 简单建筑
- 重复树木
- 重复贴图
- 空旷背景
- 简单天空盒

森林示例：

```
简单绿色地面
+
几棵重复的低模树
+
简单树干
+
绿色贴图
+
远处模糊背景
```

禁止：cinematic environment / photorealistic forest / detailed vegetation / volumetric forest / realistic terrain

## 灯光

灯光必须非常简单。

主要使用：
- 单一环境光
- 简单太阳光
- 简单三点式灯光
- 简单漫反射
- 明显阴影
- 阴影边缘略硬

可以出现：角色一侧明显偏亮 / 地面有简单阴影 / 背景亮度与角色不完全协调

这种"不够高级"的光照反而是重点。

禁止：cinematic lighting / dramatic rim light / volumetric god rays / sophisticated global illumination / Hollywood lighting / photorealistic reflections

## 色彩

颜色不要高级。更接近：

```
yellow
orange
grass green
sky blue
purple
brown
beige
```

这些很直接、很传统的动画颜色。颜色可以：
- 稍微脏
- 稍微艳
- 稍微不协调
- 不同物体之间色彩关系不够高级

保留一种"十几年前动画片的土色彩"。

禁止：高级电影调色 / 电影级色彩管理 / 精致互补色 / 现代商业视觉 / 高级HDR

## 构图

默认使用：正面 / 侧面 / 三分之二侧面 / 中景 / 半身 / 全身。

构图简单直接。主体经常位于画面中央或接近中央。

镜头像动画制作人员直接架一个虚拟摄影机拍角色。

禁止：高级电影构图 / 复杂景深 / 强烈镜头语言 / anamorphic lens / 电影级摄影机运动

## 世界参数

```yaml
world:
  terrain:
    geometry: primitive
    complexity: low

  vegetation:
    variety: low
    repetition: high

  props:
    density: low

  background:
    complexity: low

  texture:
    resolution: low

  sky:
    type: simple_skybox
```

## 世界观视觉

最终画面应该让人产生这样的感觉：

```
国产儿童动画
+
早期3D电视动画
+
低预算电脑动画
+
学生动画作业
+
小型工作室独立制作
+
奇怪但认真的角色设计
```

关键词：

```
low-budget Chinese 3D animation
early Chinese CGI animation
low-cost 3D cartoon
cheap 3D animation aesthetic
amateur 3D animation
student animation project
early 2000s CGI cartoon
old children's 3D animation
rough character modeling
simple texture mapping
awkward 3D character
```

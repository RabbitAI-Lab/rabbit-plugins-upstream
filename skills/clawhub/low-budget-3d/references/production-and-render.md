# Production Simulator & Render Degrader - 制作模拟与渲染降级

## Production Simulator

模拟"假设这是一家2000年代国产小型动画公司的制作流程，他们会怎么做？"

### Modeling

```yaml
modeling:
  polygon_budget: low
  subdivision: minimal
  topology: crude
```

### Texturing

```yaml
texturing:
  resolution: low
  uv_quality: imperfect
  repetition: medium_high
```

### Rigging

```yaml
rigging:
  complexity: low
  articulation: limited
```

### Rendering

```yaml
rendering:
  engine_quality: basic
  antialiasing: weak
  shadows: simple
```

这一层让整个 Skill 从"风格 Prompt"变成"制作条件模拟器"。

## Render Degrader

专门负责"防止模型生成得太漂亮"。这是所有同类 Prompt 最容易失败的地方。

### 降级参数

```yaml
degradation:
  detail: -60%
  material: -70%
  lighting: -50%
  texture: -60%
  geometry: -45%
  realism: -80%
  cinematic: -90%
  polish: -90%
```

### 转译为模型语言

```
low-resolution textures
weak anti-aliasing
simple diffuse shading
crude materials
basic reflections
hard shadows
limited geometric detail
slightly blurry image
visible polygon edges
simple texture mapping
outdated CGI rendering
```

## 渲染质量

这是整个风格最重要的控制项。必须主动降低：

```
rendering quality
texture resolution
anti-aliasing quality
surface detail
material complexity
geometry complexity
lighting complexity
```

画面应该具有：
- 低分辨率CG截图感
- 轻微模糊
- 轻微锯齿
- 轻微贴图失真
- 简单阴影
- 简单反射
- 不均匀边缘
- 轻微压缩感
- 老式视频截图质感

理解为：从一部2000年代国产3D动画DVD / 电视节目中截出来的一帧。

可以有轻微：

```
video compression
soft image
low-resolution texture
weak anti-aliasing
slight color bleeding
```

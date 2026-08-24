# Style Constitution - 风格宪法

## Style DNA

```yaml
style_dna:
  production:
    era: early_2000s
    origin: china
    budget: low
    studio_size: small

  modeling:
    polygon_density: low
    topology: simple
    proportions: awkward
    anatomy: simplified

  character:
    head_ratio: large
    limbs: stiff
    joints: crude
    face: simplified
    mouth: exaggerated
    eyes: unfocused

  material:
    type: primitive
    texture_resolution: low
    fur: false
    pbr: false

  environment:
    geometry: simple
    repetition: high
    detail: low
    density: sparse

  lighting:
    complexity: low
    style: direct
    shadow: hard

  rendering:
    resolution: low
    antialiasing: weak
    texture_quality: low
    compression: mild

  composition:
    complexity: low

  emotional:
    cute: low
    charming: medium
    awkward: high
    funny: high
    polished: zero
```

## 4 Rules（风格宪法）

### Rule 01：贫穷感是真实的

不是"模拟老CG"。而是模拟当时确实没有足够预算、建模能力、渲染能力的制作环境。

### Rule 02：粗糙必须贯穿整个世界

不能出现"粗糙角色 + 高级电影背景"。必须形成完整一致性：

```
粗糙角色 + 粗糙材质 + 粗糙动画 + 粗糙场景 + 粗糙灯光 + 粗糙渲染
```

### Rule 03：不要人为"艺术化"

不要把粗糙变成独立艺术电影 / A24风 / retro aesthetic。而应该是国产动画制作条件有限造成的自然结果。

### Rule 04：不要追求漂亮

允许丑。以下都是"风格资产"：
- 五官不对称
- 比例奇怪
- 动作僵硬
- 材质廉价
- 背景空
- 色彩土
- 光影普通
- 模型生硬

## Budget Level（预算等级变量）

用户可控制预算等级，实现"同一个风格，不同预算等级"。

### Level 1 - 真实参考图级别（默认）

```yaml
budget_level: 1
roughness: 0.95
awkwardness: 0.90
model_quality: 0.20
texture_quality: 0.20
animation_quality: 0.25
lighting_quality: 0.35
environment_quality: 0.30
render_quality: 0.25
```

### Level 2 - 稍微好看一点

```yaml
budget_level: 2
roughness: 0.75
awkwardness: 0.70
model_quality: 0.40
texture_quality: 0.40
animation_quality: 0.45
lighting_quality: 0.50
environment_quality: 0.45
render_quality: 0.40
```

## Style Weights（风格权重）

```yaml
model_quality: 20%
texture_quality: 15%
character_design: 20%
awkward_proportion: 15%
facial_expression: 10%
lighting: 5%
environment: 10%
rendering_artifacts: 5%
```

角色粗糙度 + 模型比例 + 表情 + 贴图质量决定风格是否成立。而不是靠 low-poly 一个关键词解决。

## Style Token（一句话风格锚定）

英文：

```
low-budget Chinese early-2000s 3D animation, rough amateur modeling, awkward proportions, stiff character posing, simple texture mapping, primitive materials, deadpan expressions, crude low-poly environment, cheap CGI rendering, simple lighting, low-resolution textures, imperfect anti-aliasing, earnest but unintentionally funny
```

中文：

```
早期2000年代国产低成本3D动画，粗糙业余建模，笨拙失衡比例，僵硬动作，简单贴图，廉价材质，木讷表情，粗糙低模场景，低质量CG渲染，简单灯光，低分辨率贴图，轻微锯齿，认真但莫名搞笑
```

# Prompt Compiler - 提示词编译器

## 编译结构

前面所有模块最终进入 Prompt Compiler。输出不是一条 Prompt，而是：

```
Prompt + Negative Prompt + Style Parameters
```

### generation YAML

```yaml
generation:
  subject:       # 从 Step 1 Intent Parser
  action:        # 从 Step 1 Intent Parser
  character:     # 从 Step 3 Subject Rebuilder + Step 4 Character Director
  environment:   # 从 Step 4 World Builder
  production:    # 从 Step 5 Production Simulator
  lighting:      # 从 Step 4 World Builder (灯光规则)
  camera:        # 从 Step 4 World Builder (构图规则)
  rendering:     # 从 Step 5 Render Degrader
  style_anchor:  # 从 Step 2 Style Constitution (Style Token)
  negative:      # 从本文件 Negative Prompt
```

## 核心 Style Prompt 模板

```text
A low-budget Chinese 3D animated film aesthetic, early 2000s Chinese children's CGI animation, rough amateur 3D character modeling, simple low-polygon geometry, awkward body proportions, oversized head, stiff arms and legs, unnatural joints, primitive facial structure, slightly unfocused eyes, thin eyebrows, exaggerated protruding mouth, slightly ape-like lips, blank and clumsy facial expression, naive and deadpan character design.

The character has no realistic fur, instead using cheap plastic-like, rough clay-like or low-quality rubbery materials, simple texture mapping, low-resolution UV textures, visible texture stretching, uneven surface details, subtle handmade modeling imperfections.

Simple direct lighting, basic ambient light, plain three-point lighting, hard and slightly crude shadows, simple diffuse shading, low-quality reflections, no cinematic lighting.

The environment is equally low-budget: simple geometric terrain, rough low-poly mountains, primitive trees, repeated textures, simple grass, basic rocks, sparse background, empty spaces, simple skybox, low-detail scenery.

The whole image should look like a frame from an old Chinese low-budget children's 3D animation, a student animation project, or a small independent animation studio production from the 2000s.

The image should feel sincere, earnest, clumsy, cheap, slightly ugly, awkward, naive and unintentionally funny.

Visible low-poly geometry, primitive modeling, simple textures, stiff animation aesthetics, imperfect rendering, low-resolution CGI, slight aliasing, soft image quality, weak anti-aliasing, basic lighting, crude materials, outdated computer graphics.

NOT polished, NOT beautiful, NOT cinematic, NOT premium CGI.
```

## Negative Prompt

```text
Pixar,
Disney,
DreamWorks,
high-end CGI,
premium 3D animation,
cinematic rendering,
photorealistic,
realistic fur,
realistic skin,
high-detail fur,
PBR materials,
subsurface scattering,
complex shaders,
global illumination,
ray tracing,
HDR,
cinematic lighting,
dramatic rim light,
volumetric lighting,
beautiful composition,
professional animation,
smooth animation,
realistic anatomy,
perfect proportions,
detailed character design,
modern AAA game graphics,
Unreal Engine cinematic render,
Octane render,
Redshift render,
hyper detailed environment,
photorealistic landscape,
glossy materials,
luxury 3D aesthetic,
anime,
Disney-like facial expressions,
cute polished mascot,
perfectly smooth surface,
ultra sharp image,
8K detail,
highly refined textures
```

## 模型适配器

根据目标平台调整 Prompt 风格：

| 平台 | 适配要点 |
|------|---------|
| GPT Image | 自然语言描述优先，风格词融入叙事句 |
| Flux | 标签式关键词优先，逗号分隔 |
| Midjourney | `--style raw` 关闭，用 `--v 6` 附加风格权重 |
| SDXL | 标签 + 权重语法 `(keyword:1.3)` |
| Nano Banana | 自然语言 + 风格标签混合 |

## 编译规则

1. 80% 靠正向风格架构控制（建模规则 + 材质规则 + 制作规则 + 灯光规则 + 渲染规则），20% 靠 Negative Prompt
2. 真正的问题不是模型不知道什么不能做，而是模型不知道"粗糙到底意味着什么"
3. 不要依赖 Negative Prompt 解决一切 - 必须用正向架构让模型理解"低成本动画生产逻辑"
4. Style Anchor（Style Token）始终嵌入 Prompt 末尾作为风格锚定

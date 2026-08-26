# 照片转《极乐迪斯科》风格 / Photo to Disco Elysium

将用户上传的人像、城市、乡镇、街道、建筑与室内照片，重构为受《极乐迪斯科》启发的心理绘画与环境概念作品。

Reconstruct user-supplied portraits, cities, towns, streets, architecture, and interiors as psychological paintings and environmental concept art inspired by *Disco Elysium*.

## 特点 / Highlights

- 人像默认使用高抽象的 `conceptual_portrait`：保留可辨识的面部拓扑与姿态，将背景改写为表达角色气质的色块、线条与象征几何。
- 可选择较温和的 `character_portrait`，在更高保真度下保留摄影中的人物信息。
- 环境图保留地点锚点、空间关系和叙事物件，同时重建色彩、边缘、明暗与心理氛围。
- 首轮先说明素材适配性，并等待确认后才生成；自然风光属于条件适配，避免把它错误处理成普通油画滤镜。
- 每一张输入照片对应一张独立输出图，不拼贴多张结果。

## 使用 / Usage

在 Codex 中上传图片后，调用：

```text
$photo-to-disco-elysium
```

For portrait inputs, choose `conceptual_portrait` (default) or `character_portrait`. For environments, the skill selects the corresponding environmental workflow.

## 内容 / Contents

```text
SKILL.md                    Core workflow and activation rules
agents/openai.yaml          Codex display metadata
references/                 Analysis cards, art direction, prompt compiler, and QA checklists
assets/skillhub-icon.png    Skill icon
```

## 授权与来源边界 / Rights and source boundary

这是一个原创的提示词与工作流包，并非官方产品，也不包含《极乐迪斯科》的角色、美术原图、截图或其他可再分发的官方资产。`Disco Elysium` 是其权利人的商标；本项目仅以其可观察到的高层视觉方法为灵感，不主张任何官方关联。

This is an original prompt-and-workflow package, not an official product. It contains no redistributable *Disco Elysium* character art, screenshots, or other official assets. `Disco Elysium` is a trademark of its respective owner; this project draws only on high-level, observable visual methods and claims no affiliation.

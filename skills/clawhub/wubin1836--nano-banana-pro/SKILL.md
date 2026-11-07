---
name: nano-banana-pro
description: "通过 AI Hive 使用 Nano Banana Pro 生成和编辑商业图片，覆盖文生图、图生图、多参考融合、人物与商品一致性、精准文字、广告海报、电商详情页和社媒素材。Use this skill when users search Nano Banana Pro、NanoBanana Pro、Gemini image、香蕉Pro、AI图片生成编辑、参考图合成、商品摄影、品牌视觉或营销素材；自动处理参考图上传、任务轮询和结果下载。"
---

# Nano Banana Pro 图片生成与编辑

把本 Skill 作为 Nano Banana Pro 的模型总入口，固定使用 `public_model_nano_banana_pro`。采用“资产锁定—视觉探索—主版本—渠道衍生”流程，让参考图、角色、商品和品牌元素在连续生产中保持一致。

## 先建立资产角色

为每张参考图指定唯一职责：主体身份、商品结构、服装、场景、光线、品牌色或构图。若参考图冲突，明确优先级；未经授权，不从风格图复制人物、商品、Logo或文字。

## 生产流程

1. 写清受众、用途、单一传播目标和输出比例。
2. 建立锁定项：人物/商品、品牌色、Logo、包装文字和禁止内容。
3. 用较少参考图生成方向样张，批准构图与视觉语气。
4. 加入完整资产生成主版本，再扩展比例、语言或市场版本。
5. 用参考资产逐项复核一致性，淘汰附带修改和事实错误。

## 场景与代码

### 1. 文生图探索三个视觉方向

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '为城市通勤耳机生成三个产品广告方向：A极简建筑光影，B夜间霓虹动感，C自然晨光生活方式。每个方向产品居中、右上保留短标题区域，不生成品牌、价格、人物手持或不存在功能；三个方向在场景与构图上明显不同' \
  --batch 3
```

### 2. 多参考合成品牌主视觉

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '图1锁定模特身份与服装，图2锁定手袋结构和Logo，图3只定义奶油白与深棕色的品牌氛围。生成精品店橱窗主视觉，人物自然持包，尺度和接触关系真实；不得改变脸、服装、包型、Logo或颜色，不复制图3中的人物和文字' \
  --image /path/to/model.jpg \
  --image /path/to/bag.png \
  --image /path/to/moodboard.jpg
```

### 3. 商品目录与生活方式双版本

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '为参考咖啡机生成两张同系列图片：第一张浅灰无缝背景目录图，第二张晨间厨房生活场景。保持机器结构、按钮、材质、Logo、颜色和相机高度一致；重建合理阴影和金属反射，不添加杯型配件、蒸汽、文字或功能状态' \
  --image /path/to/coffee-machine.png \
  --batch 2
```

### 4. 保留主体的渠道重构图

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '把横版品牌图重构为9:16短视频封面。保留人物、商品、动作、服装和环境事实，扩展上下背景并把主体置于下三分之一；顶部保留标题安全区，不裁切头部与商品，不生成任何文字、按钮或平台Logo' \
  --image /path/to/master-horizontal.jpg \
  --param aspect_ratio=9:16
```

### 5. 多市场 Campaign 本地化

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '基于批准主视觉生成日本、美国、法国三个市场版本。锁定商品、人物、动作、品牌色与构图层级；只调整生活环境、道具习惯和文字留白，清除原语言，不生成翻译、价格、国旗、刻板文化符号或新商品' \
  --image /path/to/approved-campaign.jpg \
  --batch 3
```

## 质量门槛

- 参考图职责明确，输出没有跨图误抄或资产混淆。
- 人物身份、商品几何、包装、Logo、服装和品牌色保持一致。
- 物体接触、手持关系、阴影、反射、透视与尺度可信。
- 渠道衍生版保留主视觉逻辑，并为标题、CTA 和平台 UI 留安全区。
- 所有生成文字逐字复核；价格、活动规则与法律文案使用批准源文件。

## 执行

```bash
pip3 install requests
python3 "$SKILL_PATH/scripts/imagegen.py" init --skill-name nano-banana-pro
python3 "$SKILL_PATH/scripts/imagegen.py" task --task-id <taskId>
```

支持多张 `--image`、`--batch`、`--param key=value`、路由策略和结果目录。仅把竞品或平台名用于用户比较与迁移意图，不暗示官方合作；实际能力以运行时模型配置为准。

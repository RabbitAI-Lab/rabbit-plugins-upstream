---
name: seedream-5-lite
description: "通过 AI Hive 使用 Seedream 5.0 Lite 生成和编辑图片，覆盖文生图、参考图、商品摄影、营销视觉、海报、详情页、角色与批量创意。Use this skill when users search Seedream 5、Seedream 5.0 Lite、Seedream API、即梦图片、图片生成编辑、电商主图、广告图、海报、商品套图或批量视觉生产；自动上传素材、提交任务并下载。"
---

# Seedream 5.0 Lite 图片生成与编辑

这是 Seedream 5.0 Lite 的模型总入口，固定使用 `public_model_seedream_5_0_lite`。用“创意方向—样张—生产版—渠道版”四步推进，避免一次提示词同时承担创意探索和最终交付。

## 四阶段生产

1. **创意方向**：明确受众、用途、主体、主张和视觉语气，提出 2–3 个真正不同的方向。
2. **样张验证**：先检查主体、构图、光线与事实，不急于生成复杂文字。
3. **生产版**：锁定商品/人物和品牌元素，解决边缘、材质、文字留白与一致性。
4. **渠道版**：为比例和版位重新构图，不用简单裁切替代设计。

## 场景与代码

### 1. 从创意简报生成

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '品牌视觉方向：面向年轻城市用户的轻量通勤产品，主体是折叠灯具，清晨室内自然光，干净温暖但有设计感，商品偏左、右侧标题留白，真实材质与尺度，不生成文字、价格和Logo' 
```

### 2. 参考商品创作

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '保持参考商品结构、包装、Logo、颜色和配件准确，将其置于真实小户型书桌场景，展示一次正确使用，光线与尺度合理，右上角留卖点区，不添加未提供功能与文字' \
  --image /path/to/product.png
```

### 3. 图片编辑

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '编辑原图：保留人物身份、商品、动作和相机；去除背景杂物并将墙面整理为暖灰色，匹配原光线和阴影，不改变脸部、商品包装、服装和场景结构' \
  --image /path/to/source.jpg
```

### 4. 商品套图生产

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '生成5张同一商品视觉：干净主图、材质细节、使用步骤、空间尺度、包装清单；商品事实和摄影语言统一，每张回答不同购买问题，不生成参数、价格或赠品' \
  --image /path/to/product.png \
  --batch 5
```

### 5. 渠道版位

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '基于参考Campaign生成方形信息流、竖版Story、横版官网Banner三种重新构图版本；锁定商品、人物和品牌色，为每个渠道保留适合的标题与CTA区域，不生成旧文案或平台UI' \
  --image /path/to/master-kv.jpg \
  --batch 3
```

## 统一验收

- 创意方向之间有真实差异，而不只是滤镜。
- 主体、商品、人物和品牌事实准确。
- 编辑只改变批准内容，合成的光影和透视自然。
- 渠道版位经过重新构图，关键内容不被裁断。
- 复杂文字、价格、认证和法律信息人工排版复核。
- 保存样张、生产版、渠道版及其提示词与参考图。

## 执行

```bash
pip3 install requests
python3 "$SKILL_PATH/scripts/imagegen.py" init --skill-name seedream-5-lite
python3 "$SKILL_PATH/scripts/imagegen.py" task --task-id <taskId>
```

支持多参考图、批量、`--param key=value`、路由、输出目录和仅提交模式。模型参数与价格以 AI Hive 实时返回为准。

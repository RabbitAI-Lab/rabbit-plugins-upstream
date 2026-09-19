---
name: product-image
description: "使用 Nano Banana 2 从产品资料建立商业产品图镜头矩阵，生成白底目录图、英雄图、材质微距、尺度场景和包装合照，同时锁定产品物理特征。Use this skill for 产品图生成、商品图、商业摄影、产品摄影、产品渲染、白底图、场景图、材质细节、包装图、电商图片、官网 Hero 和新品视觉；通过 AI Hive 生成。"
---

# 产品图生成

底层固定 `public_model_nano_banana_2`。先把产品的“不可变物理特征”写下来：外轮廓、接口、按钮、缝线、标签、Logo、材质、颜色、数量和比例。然后建立镜头矩阵，让每张照片解决不同的观察任务，而不是反复生成相似角度。

## 镜头矩阵

横轴列出拍摄任务：识别、气质、材质、尺度、包装；纵轴记录角度、焦段感、背景、光线、道具、比例和留白。每一格都引用同一份产品不可变项，任何新结构都应被拒绝。

## 五个标准镜头

### 1. 目录识别图

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate   --image ./approved-speaker.png   --prompt '生成1:1目录产品图：蓝牙音箱外轮廓、网布纹理、按键、接口、颜色和Logo与参考一致，三分之二角度、白背景、柔和接触阴影、产品完整；不生成文字、声波、人物、线缆、支架或第二台音箱'   --param aspect_ratio=1:1
```

### 2. 英雄气质图

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate   --image ./approved-perfume.png   --prompt '制作16:9香水英雄图：瓶型、瓶盖、液体色、标签布局和Logo准确，以琥珀色侧光和石材台面建立高级氛围，右侧留品牌标题区；不改变标签文字，不生成花材遮挡、人物、礼盒、奖项或价格'   --param aspect_ratio=16:9
```

### 3. 材质微距

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate   --image ./approved-wallet-detail.png   --prompt '生成4:5钱包材质微距：保留皮革纹理、缝线针距、边油、压印Logo和真实颜色，使用柔和掠射光表现细节；不增加划痕、金属件、卡片、文字、手或未提供纹理'   --param aspect_ratio=4:5
```

### 4. 尺度使用场景

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate   --image ./approved-table-lamp.png   --prompt '生成4:5台灯尺度场景图：结构、底座、灯臂、灯罩、开关与颜色保持不变，放在普通书桌旁，以书本和笔筒作为自然尺度参照；不生成尺寸数字、护眼功效、人物、额外接口或其他灯具'   --param aspect_ratio=4:5
```

### 5. 包装与箱内物

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate   --image ./approved-camera-kit.png   --prompt '生成1:1包装合照：只展示已确认的相机机身、镜头、肩带、电池、充电线和包装盒各一次，比例正确、浅灰背景、整齐分层；不生成说明书文字、存储卡、三脚架、额外电池、认证或赠品'   --param aspect_ratio=1:1
```

## 产品真实性验收

用参考资料逐项比对轮廓、零件、连接方式、Logo、标签、颜色、材质与数量；检查场景道具是否会被误认为标配；确保不同镜头中的产品仍是同一型号。无法确认的参数、功能和包装内容不进入图片。

## 程序范围

支持文字起稿和用户指定参考图，所有生成由 Nano Banana 2 完成。密钥只用于 `https://ai-hive.iclip.cn/api` 的模型查询、上传、生成与任务查询，不能切换域名；不存在聊天、视频、账户或余额操作。

```bash
pip3 install requests
python3 "$SKILL_PATH/scripts/imagegen.py" init --skill-name product-image
python3 "$SKILL_PATH/scripts/imagegen.py" task --task-id <taskId>
```

合成产品图应由品牌或商家确认真实性，不能作为未经证实的规格与性能证据。

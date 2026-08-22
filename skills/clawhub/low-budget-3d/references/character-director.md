# Character Director - 角色设计器

## 角色建模

简单、粗糙、低精度的3D建模。明显存在：
- 简单几何体拼接
- 低面数模型
- 较少的细分
- 方形/椭圆形/圆柱形等基础几何结构
- 身体结构不够自然
- 头部比例略大
- 躯干笨重
- 手脚简单
- 手指几乎没有细节
- 四肢略短
- 肩膀/手肘/膝盖等关节转折明显
- 身体比例微妙失衡
- 模型轮廓略显生硬

避免：完美身体比例 / 圆润流畅的高级建模 / 精致脸型 / 复杂肌肉结构 / 真实解剖结构

应该有一种：奇怪、笨拙、木讷、土气，但非常有辨识度的卡通造型。

## 脸部设计

脸部是整个风格非常重要的部分。五官结构非常简单。

### 眼睛
- 小而简单
- 略微失焦
- 视线不完全一致
- 黑色或深色虹膜
- 缺少复杂眼球反射
- 不要晶莹剔透
- 不要高级眼神

### 眉毛
- 细长
- 简单
- 像直接贴在脸上的几何线条

### 鼻子
- 简单隆起
- 粗糙
- 结构不精细

### 嘴巴（突出、宽大、夸张）
- 厚嘴唇
- 猩猩嘴
- 大嘴
- 外凸嘴部
- 简单唇线
- 像一块独立模型贴在脸部前方

### 整体表情
木讷、憨、呆、迟钝、没有精神。

```
deadpan
blank stare
slightly confused
stupidly serious
emotionally numb
awkward expression
```

禁止：cute anime expression / Pixar expression / highly expressive face / big sparkling eyes / perfect smile

## 角色动作

"动画师没有钱和时间做复杂动作"的感觉。

- 站姿僵硬
- 双臂自然垂下
- 四肢像简单骨骼绑定
- 手腕动作非常有限
- 手掌动作简单
- 腿部动作僵硬
- 身体重心不自然
- 肩膀几乎不随动作变化
- 手肘转折生硬
- 走路姿势机械
- 身体缺少自然惯性

禁止：流畅迪士尼式动作 / 高级3D动画姿态 / 动态大片动作 / 自然人体运动 / 高级运动捕捉效果

核心感觉：像一个低成本动画角色被"摆"在那里，而不是被高级动画师"演"出来。

## 材质

绝对不要真实毛发。即使是牛/熊/豹/狗等动物，也使用：
- 简单贴图
- 粗糙塑料
- 低精度材质
- 黏土质感
- 廉价橡胶
- 廉价塑料
- 粗颗粒表面
- 简单漫反射

表面可以有：简单颜色变化 / 低精度纹理 / 重复纹理 / 轻微噪点 / 不均匀贴图 / 模型接缝 / 简单UV贴图 / 轻微拉伸纹理

禁止：realistic fur / physically based fur / subsurface scattering / realistic skin / micro surface detail / glossy premium material / cinematic materials

## 贴图语言

基础颜色 + 简单纹理 + 低精度UV贴图。

豹纹不是每一根毛都有清晰的豹纹，而是一张有些模糊、有些拉伸、略微重复的豹纹贴图直接覆盖在模型表面。

树木：
- 树干 = 简单棕色纹理
- 树叶 = 一团绿色几何模型
- 草地 = 大面积绿色贴图
- 山体 = 简单颜色块 + 重复岩石纹理

## 角色设计参数

```yaml
character:
  silhouette:
  head_body_ratio:     # 头身比，默认偏大
  limb_length:         # 四肢长度，默认偏短
  body_mass:           # 躯干体积，默认笨重
  face_structure:      # 脸部结构，默认简化
  eye_design:          # 眼睛设计，默认小而呆
  eyebrow_design:      # 眉毛设计，默认细线条
  mouth_design:        # 嘴巴设计，默认突出夸张
  ear_design:
  hand_design:         # 手部设计，默认简单无细节
  foot_design:
  pose:                # 姿态，默认僵硬
  expression:          # 表情，默认木讷
  rig_quality: 0.2     # 骨骼绑定质量（1.0=高级动画绑定, 0.5=一般动画, 0.2=粗糙低成本动画）
```

`rig_quality` 默认 0.2，让"僵硬感"成为可控制变量而非形容词。

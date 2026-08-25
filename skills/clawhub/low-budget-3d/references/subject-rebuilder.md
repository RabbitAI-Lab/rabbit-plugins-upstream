# Subject Rebuilder - 视觉对象重构器

核心任务：把正常对象重新解释成"低预算国产动画版本"。

不简单变成 `panda + low poly + retro CGI`，而是重新思考：如果这是一个2000年代初国产儿童3D动画团队制作的对象，会怎么建模？

## Subject Transformation Matrix

### 动物

```
现实动物
↓
大头
↓
短肢
↓
笨重躯干
↓
简化五官
↓
夸张嘴部
↓
简单贴图
```

示例 - LowBudget3D 熊猫：

```
oversized head
short limbs
simple torso
primitive ears
simplified eyes
large protruding muzzle
simple black-and-white texture
awkward proportions
stiff pose
cheap rubber-like surface
```

### 人物

```
真人
↓
头部放大
↓
身体简化
↓
四肢僵硬
↓
手掌简化
↓
五官贴图化
↓
表情木讷
```

### 机器人

```
复杂机械
↓
基础几何体
↓
少量零件
↓
大块结构
↓
简单材质
```

### 建筑

```
真实建筑
↓
简单体块
↓
少窗户
↓
重复纹理
↓
粗糙贴图
```

### 食物

```
真实食物
↓
简化体积
↓
夸张比例
↓
颜色块
↓
塑料/橡皮泥质感
```

### 载具

```
真实载具
↓
简单车身几何
↓
少量细节
↓
重复贴图
↓
廉价塑料质感
↓
简化车轮/结构
```

## 重建规则

1. **不直接写死具体对象** - 而是建立转换策略，根据对象类型自动生成低预算版本
2. **保留辨识度** - 重建后仍需能辨认出原对象（熊猫还是熊猫，不是抽象几何体）
3. **强化土味** - 比例失衡/嘴部突出/眼神呆滞是通用特征，适用于所有类型
4. **材质统一** - 所有对象都使用 primitive material（简单贴图/粗糙塑料/黏土/廉价橡胶），绝不用真实毛发或高级材质

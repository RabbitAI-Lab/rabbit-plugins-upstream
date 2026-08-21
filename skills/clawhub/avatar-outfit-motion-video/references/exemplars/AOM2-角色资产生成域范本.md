## AOM2 角色资产生成域范本

### 域任务要求

| 任务ID | 任务类型 | 必选组件 | 组装顺序 | 约束 | 格式 |
|--------|---------|---------|---------|------|------|
| AOM2-01 | 头像生成 | 头像图、风格参数 | 风格确定→生成或处理→清晰度校验 | 正面清晰、固定种子 | PNG 头像图 |
| AOM2-02 | 服装生成 | 服装图、款式参数 | 款式确定→生成→干净背景校验 | 平铺或干净背景 | PNG 服装图 |
| AOM2-03 | 三视图合成 | 头像图、服装图、三视图提示词、正面单图提示词 | 双垫图→特征剥离→三视图→派生正面单图 | 三视角一致、固定种子 | PNG 三视图 + PNG 正面单图 |

### AOM2-01 头像生成范本

**适用场景**：随机生成或按描述生成角色脸，锁定身份基础。

**输入**：风格参数、角色描述。

**输出**：正面清晰头像图。

**范本内容**：

```
portrait of a [角色描述], [发色] [发型], [五官特征], facing camera,
clean background, high detail, realistic photography style, studio lighting.
```

**样本特征摘要**：
- 结构：角色外观 → 发型 → 五官 → 机位 → 风格 → 打光
- 风格：写实影棚人像
- 逻辑：先定身份特征，再定环境与风格
- 格式：英文提示词，逗号分隔短语

---

### AOM2-02 服装生成范本

**适用场景**：随机生成或按描述生成服装参考图。

**输入**：款式关键词、风格。

**输出**：平铺或干净背景服装图。

**范本内容**：

```
[服装款式描述], flat lay on clean background, full garment visible,
no model, no watermark, high detail, studio lighting.
```

**样本特征摘要**：
- 结构：款式 → 平铺/干净背景 → 完整展示 → 无模特
- 风格：电商平铺图
- 逻辑：强调「无模特、完整展示」避免遮挡
- 格式：英文提示词短语

---

### AOM2-03 三视图合成范本

**适用场景**：特征剥离法合成三视图，并派生正面单图作视频首帧。

**输入**：头像图（图1）、服装图（图2）。

**输出**：正面/侧面/背面三视图 + 正面全身单图。

**范本内容**：

```
character turnaround sheet, three views of the same person standing side by side in a row:
front view, side view, back view, orthographic projection, full body, white background.
consistent face, hairstyle and outfit across all three views, same height and posture,
high detail, realistic photography style, studio lighting.
```

特征剥离指令（双垫图通道解绑）：

```
主体1的面部特征与身份严格参考图片1。
主体1的服装款式与材质严格参考图片2。
```

正面单图派生（基元内分步校准点，锁定首帧身份）：

```
full body portrait of a single [角色描述] standing front view, [发色] [发型],
[服装描述], neutral relaxed standing pose, facing camera, white studio background,
realistic photography, high detail, consistent with the turnaround sheet character.
```

**样本特征摘要**：
- 结构：三视图术语 → 三视角 → 一致性要求 → 风格；后接正面单图派生
- 风格：角色设定图（character sheet）
- 逻辑：先声明三视图格式，锁定一致性，再派生首帧（分步校准）
- 格式：英文提示词 + 中文解绑指令

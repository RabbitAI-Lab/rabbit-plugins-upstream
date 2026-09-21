# 08 Overlap 计算（仅 MUST 集合 vs 可选标签）

> 已按你的口径更新：Overlap 不做两两全组合；只计算「每个可选标签 x 与 MUST 标签集合 M」的重叠度。

## 1. 定义
- MUST 集合：M = {m1..mk}
- MUST 基准量级：|M|
- 可选标签 x 的重叠量级：|M ∩ x|
- 重叠率（占 MUST 比例）：r(x) = |M∩x| / |M|
- 收窄率：s(x) = 1 - r(x)

## 2. 计算步骤（执行层）
### 2.1 计算 MUST 基准人群 |M|
1) 以 m1 AND m2 AND ... AND mk 创建组合人群（基准人群）
2) 轮询任务状态，取 audienceAmount 作为 |M|，并记录 audienceId_M

### 2.2 逐个计算可选标签 x 的 |M∩x|
对每个 x（PREFERRED/OPTIONAL）：
1) 创建组合人群：audienceId_M AND tag(x)
2) 轮询任务状态，取 audienceAmount 作为 |M∩x|
3) 计算 r(x)、s(x)

## 3. 输出格式（建议）
| 可选标签x | |M| | |M∩x| | 重叠率r | 收窄率s | 建议 |
|---|---:|---:|---:|---:|---|

## 4. 规模控制建议
- 优先对 PREFERRED 全量计算；OPTIONAL 只算 TopK（如 5~10 个）
- 结果缓存：同一（租户/trackType/idTypes/MUST集合/x）可缓存一段时间

## 5. 失败与兜底
- 任务失败：记录失败原因，提示用户稍后重试或替换标签
- |M|=0：直接回到标签选择/组合环节，不继续计算 overlap

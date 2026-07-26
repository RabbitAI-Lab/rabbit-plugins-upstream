# 示例

## Small 独立修复

目标：修复一个可复现的导出缺陷。

- 规模：Small；
- 治理：Lite；
- 阶段：复现、修复、回归、导出产物检查；
- 文件：Active Packet 和 Loop Runs；
- 自动验证与导出产物都通过后才可自验收。

不要创建 Program 或 Milestone。

## Medium 受治理功能

目标：增加一个横跨 API 和 UI 的用户流程。

- 规模：Medium；
- 治理：Standard；
- 第 1–3 阶段：基线和垂直切片；
- 第 3 阶段：方向对齐；
- 第 4–6 阶段：集成和主用户流程；
- 第 6 阶段：方向对齐；
- 最后设置 `Ready for Review`，由独立 QA 验收。

Developer 不能根据自己的证据签收。

## 长时间运行开始偏离

第 6 阶段测试通过，但交付流程已不再解决 Owner 原始问题：

- 建议 `Locally Compliant, Globally Misaligned`；
- 停止扩展功能；
- 保留局部证据；
- 由治理层比较原始结果、当前行为和新假设；
- 只有重新对齐或重基线后才能继续。

## 重复失败

两个 Loop 连续失败且没有缩小根因：

- 停止扩大修改；
- 记录失败命令和证据；
- 有界诊断存在时设置 `Needs Fix`；
- 缺少环境或权限时设置 `Blocked`；
- 不能重置成新 Milestone。

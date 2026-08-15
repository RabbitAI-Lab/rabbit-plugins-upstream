---
name: backup-restore
description: "备份恢复管理器，定时备份关键数据（MEMORY.md、训练数据、模型权重、配置文件），支持快速恢复和灾难演练。 增强方法(v1.1): SHA256重复检测(避免备份冗余)、感知哈希检测相似图片、文件版本管理(保留最近3个版本+一键恢复)。 触发词: 备份数据/恢复数据/灾难演练/检查备份 不触发: 日志分析/性能监控/模型训练 (DEF-56激活版)"
version: 1.1.0
user-invocable: true
tools: [read, exec]
dependencies: []
metadata:
  layer: infrastructure
  priority: P1
  category: infra-ops
  openclaw:
    emoji: "💾"
    os: ["win32", "linux", "darwin"]
    requires:
      bins: ["python", "git"]
---

> **核心功能**: 本技能提供(保留最近3个版本+一键恢复)、(避免备份冗余)、相似图片等能力。


# Backup Restore Skill

## 使用场景

1. **定时自动备份**: Cron每日01:00-04:00分时段备份Skills/配置/训练数据/模型权重,确保数据安全
2. **灾难恢复**: 系统故障/数据丢失时,通过backup_id快速恢复到最近可用备份点,缩短停机时间
3. **版本回滚**: 升级失败或配置错误时,恢复到升级前的备份版本,支持快速回滚
4. **灾难演练**: 定期模拟故障场景,验证备份可用性和恢复流程有效性,确保RTO<30分钟
5. **磁盘空间治理**: 备份前检查磁盘空间(≥10GB),不足时自动清理过期备份,避免备份失败
6. **数据迁移**: 跨环境部署时,通过备份-恢复流程迁移MEMORY.md/配置/Skills等关键数据

## 功能说明
管理关键数据的备份和恢复，包括：MEMORY.md、训练数据、模型权重、配置文件、Skill 定义，支持定时备份、手动备份、快速恢复、灾难演练。

## 备份内容

| 数据类型 | 备份频率 | 保留周期 | 说明 |
|:---------|:---------|:---------|:-----|
| **MEMORY.md** | 每小时 | 7天 | 长期记忆文件 |
| **训练数据** | 每日 03:00 | 30天 | training_data/ 目录 |
| **模型权重** | 每周日 04:00 | 90天 | models/ 目录 |
| **配置文件** | 每日 02:00 | 30天 | docker/data/openclaw/ 目录 |
| **Skills** | 每日 01:00 | 30天 | skills/ 目录 |
| **Git 仓库** | 实时 | 永久 | 自动 git commit |

## 工作流程

### 定时备份流程（每日）

1. Cron 定时触发
2. 检查磁盘空间（至少保留 10GB）
3. 创建压缩包（ZIP 格式）
4. 计算 SHA256 校验和
5. 上传到备份存储（本地/云端）
6. 清理过期备份
7. 记录备份日志到 `memory/backups/YYYY-MM-DD.md`

### 恢复流程

1. 选择备份点
2. 验证校验和
3. 停止相关服务
4. 解压备份文件
5. 恢复到原位置
6. 验证数据完整性
7. 重启服务
8. 推送恢复完成通知

### 灾难演练流程

1. 模拟故障场景
2. 执行恢复流程
3. 验证系统功能
4. 生成演练报告
5. 推送演练结果

## 输入格式

```json
{
  "action": "backup",
  "backup_type": "full",
  "verify": true
}
```

```json
{
  "action": "restore",
  "backup_id": "backup_20260414_001",
  "verify": true
}
```

## 输出格式

```json
{
  "success": true,
  "data": {
    "backup_id": "backup_20260414_001",
    "backup_type": "full",
    "size_mb": 256,
    "checksum": "sha256:abc123...",
    "backup_path": "backups/2026-04-14_full.zip",
    "verified": true
  },
  "error": null,
  "code": "BACKUP-SUCCESS-01"
}
```

## 异常处理

| 异常编号 | 错误代码 | 触发条件 | 处理方式 |
|:---------|:---------|:---------|:---------|
| BR-ERR-01 | INSUFFICIENT_DISK_SPACE | 磁盘空间不足 | 告警+清理旧备份+重试 |
| BR-ERR-02 | BACKUP_FAILED | 备份执行失败 | 重试3次→告警CEO |
| BR-ERR-03 | CHECKSUM_MISMATCH | 校验和不匹配 | 标记备份损坏+告警 |
| BR-ERR-04 | RESTORE_FAILED | 恢复执行失败 | 回滚+告警+尝试其他备份 |

## 示例

### 全量备份

1. 输入: `{action:"backup", backup_type:"full", verify:true}`
2. 执行: 检查磁盘空间→创建ZIP压缩包→计算SHA256→存储至backups/→清理过期备份→记录日志
3. 输出: `{success:true, data:{backup_id:"backup_20260414_001", backup_type:"full", size_mb:256, checksum:"sha256:abc123...", backup_path:"backups/2026-04-14_full.zip", verified:true}}`

### 恢复数据(含校验失败异常)

1. 输入: `{action:"restore", backup_id:"backup_20260414_001", verify:true}`
2. 执行: 验证SHA256校验和→停止服务→解压恢复→验证数据完整性→重启服务
3. 校验失败输出: `{success:false, data:{backup_id:"backup_20260414_001"}, error:"校验和不匹配,备份文件可能损坏", code:"CHECKSUM_MISMATCH"}`

## 变更历史

| 版本 | 日期 | 变更说明 |
|:-----|:-----|:---------|
| v1.1.0 | 2026-06-02 | DEF-56激活版,dependencies改为[data-backup-daily] |
| v1.1.1 | 2026-06-05 | DEF-30修复:移除不存在的data-backup-daily依赖(该id为Cron任务而非Skill),dependencies改为[] |
| v1.0.0 | 2026-04-14 | 初始实现 |

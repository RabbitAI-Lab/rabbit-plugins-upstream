# PlantUML 图表类型速查

| 图表类型 | 关键字/标记 | 用途 |
|---------|-----------|------|
| 时序图 | @startuml + participant | 对象间消息交互 |
| 类图 | @startuml + class | 类结构与关系 |
| 活动图 | @startuml + start/stop | 工作流与流程 |
| 用例图 | @startuml + actor/usecase | 系统功能与角色 |
| 状态图 | @startuml + [*] | 对象状态转换 |
| 组件图 | @startuml + component | 组件组织与依赖 |
| 部署图 | @startuml + node | 硬件部署架构 |
| 定时图 | @startuml + clock/binary | 时间约束与信号 |
| 思维导图 | @startmindmap | 思维发散与组织 |
| 甘特图 | @startgantt | 项目进度规划 |

## 箭头速查

### 时序图
- `->` 实线箭头
- `-->` 虚线箭头
- `->>` 实线开放箭头
- `x>` 末端X

### 类图关系
- `--|>` 继承
- `..|>` 实现
- `-->` 关联
- `--*` 组合
- `o--` 聚合
- `..>` 依赖

### 通用连接
- `--` 实线
- `..` 虚线
- `-->` 箭头
- `-[hidden]->` 隐藏箭头

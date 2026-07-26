# CRUD 微服务拆解模板

## 第一层：业务拆解

- 实体：[实体名称]
- 核心操作：增删改查
- 附加操作：[列表分页/搜索筛选/批量操作]
- 优先级：[P0/P1/P2]

## 第二层：工程拆解

```
[实体表]
  ↓
[Repository 层]
  ↓
[Service 层] → [DTO 映射]
  ↓
[Controller 层] → [异常处理]
  ↓
[单元测试] + [集成测试]
```

## 第三层：执行拆解

| 任务 | Agent | 依赖 | 并行 |
|:------|:------|:------|:------|
| Entity + Repository + 迁移脚本 | backend-agent | 无 | — |
| Service + DTO | backend-agent | Entity+Repo | ∥ 下一行 |
| Controller + 异常处理 | backend-agent | Entity+Repo | ∥ 上一行 |
| 单元测试 + 集成测试 | qa-agent | Controller | — |

## 原子任务模板

```markdown
任务：{服务名} - {实体名} CRUD 实现
Agent：backend-agent
输入：实体定义、API 规范
输出：Entity.java, Repository.java, Service.java, Controller.java, DTO.java
验收：
- [ ] 文件存在性验证：ls 确认 5 个文件已创建
- [ ] POST /api/{entity} → 201 + 返回创建对象
- [ ] GET /api/{entity}/{id} → 200 + 返回对象
- [ ] GET /api/{entity}?page=0&size=10 → 200 + 分页列表
- [ ] PUT /api/{entity}/{id} → 200 + 返回更新对象
- [ ] DELETE /api/{entity}/{id} → 204
- [ ] 缺少必填字段 → 400 + 具体字段名
- [ ] jar tf 确认 class 文件存在
```

# 前端列表页拆解模板

## 第一层：业务拆解

- 页面：[页面名称]
- 功能：列表展示 / 筛选 / 分页 / 详情跳转 / 新建/编辑
- 数据源：[API 端点]
- 优先级：[P0/P1/P2]

## 第二层：工程拆解

```
[API 数据层: types + fetch 函数]
  ↓
[列表组件] ← [筛选组件]
  ↓           ↓
[分页组件]   [表单组件（新建/编辑）]
  ↓
[路由配置]
```

## 第三层：执行拆解

| 任务 | Agent | 依赖 | 并行 |
|:------|:------|:------|:------|
| API 层 + TypeScript 类型 | frontend-agent | 无 | — |
| 列表组件 + 筛选 + 分页 | frontend-agent | API 层 | ∥ 下一行 |
| 表单组件（新建/编辑） | frontend-agent | API 层 | ∥ 上一行 |
| 路由 + 集成 + 降级 Mock | frontend-agent | 列表+表单 | — |

## 原子任务模板

```markdown
任务：{页面名} - 列表页实现
Agent：frontend-agent
输入：API 端点定义、字段映射
输出：types.ts, api.ts, ListPage.tsx, FilterBar.tsx, Pagination.tsx
验收：
- [ ] 文件存在性验证：ls 确认所有文件已创建
- [ ] 页面正常加载不白屏
- [ ] 列表数据正确渲染
- [ ] 筛选条件变更触发重新请求
- [ ] 分页切换正常
- [ ] API 返回空数组时显示空状态（非白屏）
- [ ] API 失败时降级显示 Mock 数据或错误提示
- [ ] 所有数值用 ?? 保护（.toLocaleString() 前非 undefined）
- [ ] STATUS_MAP 覆盖所有后端枚举值
```

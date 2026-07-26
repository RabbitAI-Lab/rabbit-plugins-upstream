# 搜索技巧与分类参考

## 搜索策略

### 从窄到宽
先用精确的 3-4 词组合搜索，结果少再逐步放宽：
```
react testing jest       # 精确
react testing            # 放宽
testing                  # 泛搜索
```

### 领域+动作配对
搜索时组合领域词和动作词，命中率更高：
```
react testing       ✅ 好
testing             ❌ 太泛
how to test react   ❌ 太多噪音
```

### 同义词轮换
同一概念尝试不同表达，分别搜索：
- 部署: `deploy` / `deployment` / `ci-cd` / `release`
- 代码审查: `review` / `pr-review` / `code-review`
- 测试: `testing` / `test` / `e2e` / `unit-test`
- 文档: `docs` / `documentation` / `readme` / `changelog`
- 监控: `monitor` / `monitoring` / `observability` / `logging`

### 中英转换
中文需求 → 英文关键词搜索（英文生态技能更多）：
- "帮我写简历" → `resume generator`
- "小红书文案" → `social media content`
- "股票分析" → `stock analysis`

### 场景驱动搜索
用户说的不是技术词汇时，转换为场景关键词：
- "我要做个落地页" → `landing page` / `web design`
- "帮我准备面试" → `interview` / `leetcode`
- "想学 Rust" → `rust tutorial` / `rust best practices`

## 热门技能源

这些是高质量技能的集中地，优先检查：

| 来源 | 特点 | 典型技能 |
|------|------|---------|
| `vercel-labs/agent-skills` | React/Next.js/设计 | frontend-design, react-best-practices |
| `anthropics/skills` | 前端设计、文档处理 | frontend-design, pdf |
| `openclaw/clawhub` | 技能注册中心 | 搜索入口 |
| `skills.sh` leaderboard | 按安装量排名 | 实时热门 |

## 结果评估

### 安装量等级参考
| 等级 | 安装量 | 建议 |
|------|--------|------|
| 热门 | 10K+ | 放心推荐 |
| 成熟 | 1K-10K | 推荐 |
| 成长 | 100-1K | 可用，标注"较新" |
| 新/冷门 | <100 | 谨慎，标注"低活跃" |

### GitHub Stars 参考
| 等级 | Stars | 建议 |
|------|-------|------|
| 热门 | 1K+ | 活跃社区 |
| 稳定 | 100-1K | 可用 |
| 初期 | <100 | 标注"新项目" |

## 无结果时的处理

1. **同义词重试**: 换一组关键词再搜
2. **放宽条件**: 去掉限定词，用更泛的关键词
3. **GitHub 兜底**: skills.sh 无结果时，用 `gh search repos` 搜
4. **直接帮助**: 三源均无结果，告诉用户并直接用通用能力完成任务
5. **建议创建**: 如果用户频繁需要该能力，建议 `npx skills init` 自行创建
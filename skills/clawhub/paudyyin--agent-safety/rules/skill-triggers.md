---
name: python-coding-trigger
enabled: true
event: PreTask
task_type: "coding"
files_pattern: "\\.py$"
skill: python-reviewer
priority: 10
---
当任务涉及 Python 编码时，自动加载 python-reviewer 技能上下文。

---
name: typescript-coding-trigger
enabled: true
event: PreTask
task_type: "coding"
files_pattern: "\\.(ts|tsx|js|jsx)$"
skill: typescript-reviewer
priority: 10
---
当任务涉及 TypeScript/JavaScript 编码时，自动加载 typescript-reviewer 技能上下文。

---
name: review-trigger
enabled: true
event: PreTask
keywords_pattern: "review|审查|代码审查|code review"
skill: code-reviewer
priority: 20
---
当任务包含"review"或"审查"关键词时，自动加载 code-reviewer 技能。

---
name: security-trigger
enabled: true
event: PreTask
keywords_pattern: "security|安全|漏洞|vulnerability|凭证|credential"
skill: security-auditor
priority: 30
---
当任务涉及安全相关关键词时，自动加载 security-auditor 技能。

---
name: test-trigger
enabled: true
event: PreTask
keywords_pattern: "test|测试|coverage|覆盖率|TDD"
skill: test-engineer
priority: 15
---
当任务涉及测试相关关键词时，自动加载 test-engineer 技能。

---
name: architecture-trigger
enabled: true
event: PreTask
keywords_pattern: "architecture|架构|模块|依赖|设计模式|design pattern"
skill: architecture-critic
priority: 25
---
当任务涉及架构设计相关关键词时，自动加载 architecture-critic 技能。

---
name: performance-trigger
enabled: true
event: PreTask
keywords_pattern: "performance|性能|优化|bottleneck|瓶颈|benchmark"
skill: performance-analyst
priority: 25
---
当任务涉及性能优化相关关键词时，自动加载 performance-analyst 技能。

---
name: documentation-trigger
enabled: true
event: PreTask
keywords_pattern: "documentation|文档|API doc|注释|comment"
skill: documentation-checker
priority: 15
---
当任务涉及文档相关关键词时，自动加载 documentation-checker 技能。

---
name: maintainability-trigger
enabled: true
event: PreTask
keywords_pattern: "maintainability|可维护性|技术债务|tech debt|重构|refactor"
skill: maintainability-reviewer
priority: 20
---
当任务涉及可维护性相关关键词时，自动加载 maintainability-reviewer 技能。

---
name: explore-trigger
enabled: true
event: PreTask
keywords_pattern: "explore|侦察|查看|看看|多大|多少|有没有|是否"
skill: explore
priority: 5
---
当任务涉及快速侦察相关关键词时，自动加载 explore 代理。

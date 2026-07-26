# 测试：zhihu-research-page

## 测试 1：2% 极速版本
Input: /zhihu-research-page 执行2%版本
主题：什么是 Docker？
Expected behavior:
  - 自动搜索 ≥10 次
  - 生成 3 章节 HTML，约 2,000 字
  - HTML 含 zh-header、zh-sidebar、zh-main 结构
  - 所有 <code> 标签开闭匹配
  - 约 2 分钟完成

## 测试 2：完整版本
Input: /zhihu-research-page 执行100%版本
主题：Python 装饰器原理与应用
Expected behavior:
  - 自动搜索 ≥500 次
  - 生成 10 章节 HTML，每章 ≥11,000 字，总计 ≥100,000 字
  - 每章含独立答主身份和头像（DiceBear）
  - 侧栏导航与章节锚点一致
  - 无编造 URL，所有链接可验证

## 测试 3：教程/学习模式
Input: /zhihu-research-page 执行30%版本
主题：新手怎么学 Git？
Expected behavior:
  - 自动识别"学习"关键词，启用教程模式
  - 每章含前置知识标注、操作步骤、常见报错
  - 写作风格面向零基础读者

## 测试 4：空输入处理
Input: /zhihu-research-page
Expected behavior:
  - 从当前对话上下文自动提炼研究主题
  - 不追问用户（按阶段 0 的铁律执行）
  - 若上下文也无主题，才询问用户

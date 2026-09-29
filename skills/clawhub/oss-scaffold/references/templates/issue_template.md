<!-- Issue 模板（bug_report + feature_request 二合一骨架，实例化时拆成 .github/ISSUE_TEMPLATE/bug_report.md 与 feature_request.md 两个文件）。骨架+占位符；默认英文。 -->

<!-- ===== bug_report.md ===== -->

---
name: Bug report
about: Report something that doesn't work as expected
labels: bug
---

**Describe the bug**

{{bug_description}}

**To Reproduce**

Steps to reproduce the behavior:

1. {{step_1}}
2. {{step_2}}

**Expected behavior**

{{expected_behavior}}

**Environment**

- Version: {{version}}
- OS: {{os}}
- Related config: {{config}}

<!-- ===== feature_request.md ===== -->

---
name: Feature request
about: Suggest an idea for {{project_name}}
labels: enhancement
---

**Is your feature request related to a problem?**

{{problem_statement}}

**Describe the solution you'd like**

{{proposed_solution}}

**Describe alternatives you've considered**

{{alternatives}}

**Additional context**

{{additional_context}}

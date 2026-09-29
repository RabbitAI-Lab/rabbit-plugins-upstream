name: 功能建议 / Feature request
description: 提出一个新功能或改进建议 / Suggest a new feature or improvement
labels: ['feature request']
body:
  - type: textarea
    id: problem
    attributes:
      label: 你的场景 / Your use case
      description: 这个功能解决什么问题 / What problem does this solve
    validations:
      required: true
  - type: textarea
    id: solution
    attributes:
      label: 期望的方案 / Proposed solution
      description: 你希望它怎么工作 / How you expect it to work
    validations:
      required: true
  - type: textarea
    id: alternatives
    attributes:
      label: 备选方案 / Alternatives considered
    validations:
      required: false
  - type: checkboxes
    id: checks
    attributes:
      label: 自检 / Checklist
      options:
        - label: 我已搜索过相关 issue / I have searched for existing issues
          required: true
        - label: 这不是某个缺陷的修复请求（缺陷请走 Bug 反馈）/ This is not a bug report
          required: true

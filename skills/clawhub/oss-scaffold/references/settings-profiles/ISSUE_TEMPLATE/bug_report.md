name: Bug 反馈 / Bug report
description: 报告一个缺陷，帮助我们把项目做得更好 / Report a defect to help us improve
labels: ['bug']
body:
  - type: markdown
    attributes:
      value: |
        感谢反馈！请先搜索已有 issue，避免重复提交。
        Thanks for reporting! Please search existing issues first to avoid duplicates.
  - type: textarea
    id: what-happened
    attributes:
      label: 问题描述 / Description
      description: 发生了什么、期望是什么 / What happened and what did you expect
    validations:
      required: true
  - type: textarea
    id: reproduce
    attributes:
      label: 复现步骤 / Steps to reproduce
      placeholder: |
        1. ...
        2. ...
    validations:
      required: true
  - type: textarea
    id: env
    attributes:
      label: 环境 / Environment
      description: 版本号、操作系统、编译器或运行时等 / version, OS, compiler or runtime
      placeholder: e.g. v1.0.0 / Ubuntu 22.04 / Node 20 / Android API 30
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: 日志或截图 / Logs or screenshots
      description: 如有报错日志请附上 / Attach error logs if any
    validations:
      required: false
  - type: checkboxes
    id: checks
    attributes:
      label: 自检 / Checklist
      options:
        - label: 我已搜索过相关 issue / I have searched for existing issues
          required: true

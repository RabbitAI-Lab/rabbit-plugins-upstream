# AVAILABILITY() 货源与库存判断

**Skill ID:** `zayn-availability`
- 所属分类：询价与报价
- 一句话用途：规范不同货源状态，避免把不稳定信息写成现货
- 当前版本：`v0.1`
- 当前状态：Draft for testing
- 规则是否完成：是，初版规则已建立
- 是否已有测试案例：否，等待真实脱敏案例
- 下一步待办：测试参数解析、最低运行条件、判断规则、风险边界和输出结构

AVAILABILITY() 用于规范“有货”“可调货”“预计可供”“供应商口头反馈”“需要锁货确认”等不同货源状态。它不负责直接报价，也不允许把不稳定信息写成现货。

完整规则见 [SKILL.md](SKILL.md)，调用模板见 [examples.md](examples.md)，测试要求见 [tests.md](tests.md)。

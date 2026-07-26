## Description: <br>
DIY装机助手 helps users plan, upgrade, complete, and review Chinese-market desktop PC configurations using bundled hardware data, pricing rules, FPS references, and compatibility checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT No Attribution <br>


## Use Case: <br>
External users use this skill to translate budgets, workloads, aesthetics, upgrades, and compatibility questions into desktop PC part recommendations and pre-purchase review points. It is focused on Chinese-market PC hardware and RMB pricing. <br>

### Deployment Geography for Use: <br>
Global; recommendations are scoped to Chinese-market desktop PC parts and RMB pricing. <br>

## Known Risks and Mitigations: <br>
Risk: PC part prices, availability, and compatibility details can change after the bundled data was prepared. <br>
Mitigation: Verify final retailer pricing and manufacturer specifications before purchase, especially when prices are stale or real-time pricing is requested. <br>
Risk: The skill can run local Python scripts over its bundled hardware database. <br>
Mitigation: Review and scan the skill before deployment, and run the scripts only in a trusted workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/zhuangji-assistant-skill) <br>
- [需求路由](references/routing.md) <br>
- [通用选件策略](references/selection-policy.md) <br>
- [场景细则](references/scenarios.md) <br>
- [工作模式](references/workflows.md) <br>
- [兼容性检查](references/compatibility.md) <br>
- [价格规则](references/pricing.md) <br>
- [游戏帧率参考](references/game-performance.md) <br>
- [硬件知识问答](references/hardware-faq.md) <br>
- [硬件范围](references/hardware-scope.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown text with PC part lists, RMB prices, compatibility conclusions, tradeoff rationale, and pre-purchase review notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses price reference dates and avoids unverified model, price, FPS, or compatibility claims.] <br>

## Skill Version(s): <br>
0.0.27 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

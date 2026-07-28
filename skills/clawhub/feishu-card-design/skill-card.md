## Description: <br>
Provides Feishu/Lark IM Card 2.0 design guidance, color and layout rules, templates, examples, and local Python tools for generating and validating card JSON; it does not send messages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use this skill to create or validate Feishu/Lark Card 2.0 JSON for reports, alerts, status updates, and notifications with consistent naming, colors, layout, compatibility, and accessibility. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Example buttons or fallback messaging may imply actions outside an integrator's intended Feishu permissions. <br>
Mitigation: Review the example buttons and fallback text before deployment, and remove or replace actions that the agent should not offer. <br>
Risk: Sending cards can expose content or recipients if credentials and message delivery are coupled directly to generation. <br>
Mitigation: Keep Feishu credentials and message-sending tools separate from this skill, and require user confirmation before sending generated cards. <br>
Risk: Generated Card 2.0 JSON may be malformed or inconsistent with the skill's design rules if templates are edited. <br>
Mitigation: Run the included card validator and review generated card JSON before deployment or automated sending. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardwason/skills/feishu-card-design) <br>
- [Project homepage](https://github.com/EdwardWason/feishu-card-design) <br>
- [Feishu Card 2.0 overview](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/card-components/overview) <br>
- [Feishu card color enumerations](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/enumerations-for-fields-related-to-color) <br>
- [Card 2.0 schema](references/card-2.0-schema.md) <br>
- [Color system](references/color-system.md) <br>
- [Title naming](references/title-naming.md) <br>
- [Layout patterns](references/layout-patterns.md) <br>
- [Compatibility](references/compatibility.md) <br>
- [Accessibility](references/accessibility.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, JSON Card 2.0 templates/examples, Python helper code, and shell commands for local validation or conversion.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local Feishu/Lark card JSON; actual message sending and credentials remain outside the skill.] <br>

## Skill Version(s): <br>
1.0.5 (source: SKILL.md frontmatter, plugin.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Helps developers, support teams, SaaS operators, and users turn vague error messages into clearer guidance that explains what failed, why it failed, and what action to take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and end users use this skill to produce clearer error-message copy, debugging workflows, checklists, analysis, code changes, or decision support. It is intended for support and product-quality work where users need actionable next steps from unclear failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has broad activation wording and may be invoked for general debugging or support requests that are not specifically about improving error messages. <br>
Mitigation: Use it when the requested outcome involves clarifying an error, troubleshooting message, support response, validation feedback, or related workflow; choose a narrower debugging skill for unrelated failures. <br>
Risk: Generated wording or workflow recommendations could be inaccurate if the underlying failure context is incomplete. <br>
Mitigation: Validate proposed messages and next steps against logs, product behavior, and support criteria before publishing or applying changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/error-message-improver) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Chatflow/Workflow Agent backend issue](https://github.com/langgenius/dify/issues/39161) <br>
- [ASK HN: Why has technology become so unreliable?](https://news.ycombinator.com/item?id=49056900) <br>
- [vg error message issue](https://github.com/vgteam/vg/issues/4974) <br>
- [Enhance form validation with real-time feedback](https://github.com/Arenax-gaming/ArenaX/issues/830) <br>
- [Frontend error taxonomy issue](https://github.com/Waffle-finance/waffle-finance-core/issues/320) <br>
- [SegmentFault error-messages topic](https://segmentfault.com/t/error-messages) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with optional code blocks, shell commands, checklists, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, validation notes, and follow-up risks.] <br>

## Skill Version(s): <br>
0.20260728.40429 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

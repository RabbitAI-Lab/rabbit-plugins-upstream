## Description: <br>
根据成交证据、时间紧迫度、项目价值、当前卡点和所需投入，安排今日优先推进的客户与动作。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer-facing teams and operators use this skill to decide which candidate customers and actions to prioritize today based on confirmed deal evidence, urgency, value, blockers, and required effort. It helps structure a daily action plan while stopping formal analysis when required customer status, time, goal, or reliable evidence is missing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer lists and deal details may contain sensitive customer information shared in the agent session. <br>
Mitigation: Minimize or desensitize customer data before use, and only include information appropriate for the agent session. <br>
Risk: A generated priority ranking may be mistaken for an authoritative business decision. <br>
Mitigation: Use the ranking as decision support and preserve human-confirmed facts, classifications, owners, and original records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-priority) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zaynpeng) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with parameter status, prioritized customer lists, rationale, actions, deferred customers, and risk reminders] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided candidate customers, current status, available time, sorting goal, and at least one reliable evidence item before formal analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

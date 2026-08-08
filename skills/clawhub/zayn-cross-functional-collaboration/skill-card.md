## Description: <br>
Helps users structure cross-functional coordination by separating confirmed facts, user judgments, and unverified information while avoiding premature commitments, blame, emotional phrasing, and unsupported responsibility claims. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and operations, sales, product, engineering, project management, finance, HR, and support teams use this skill to turn cross-department updates, requests, risks, blockers, and follow-ups into clear internal coordination messages. It is intended to keep facts, assumptions, missing information, owners, timing, and next steps distinct before a user sends or escalates communication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may include unnecessary confidential business context while asking for help drafting internal coordination messages. <br>
Mitigation: Share only the minimum facts needed for the coordination task and avoid credentials, secrets, or unrelated sensitive details. <br>
Risk: Generated messages may still require human review because they can affect responsibilities, timelines, or sensitive business relationships. <br>
Mitigation: Review the draft before sending and confirm owners, deadlines, and external commitments with the relevant teams. <br>
Risk: Incomplete or unverified input could be mistaken for confirmed project status. <br>
Mitigation: Keep confirmed facts, user judgments, and pending information separate, and use conservative interim wording when key details are missing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-cross-functional-collaboration) <br>
- [Decision Rules](artifact/references/decision_rules.md) <br>
- [Output Templates](artifact/references/output_templates.md) <br>
- [Scenario Examples](artifact/references/scenario_examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-style structured response with status tables, risk notes, next actions, and draft internal messages when enough information is available.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask concise follow-up questions or provide a conservative interim message when required context is missing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact documentation states v0.1.0 draft for testing) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Family Cultivation Coach helps caregivers create and adjust weekly child-development schedules, check time conflicts, and generate family reviews while keeping storage and external integrations opt-in. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangchao228](https://clawhub.ai/user/yangchao228) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers and family assistants use this skill to turn family constraints, child preferences, and development goals into practical weekly schedules, updates, reviews, and risk reminders. It can also guide optional Feishu or Notion persistence after explicit user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process sensitive child and household routine details. <br>
Mitigation: Use nicknames or initials, avoid directly identifying details, and keep planning session-only unless the user explicitly chooses storage. <br>
Risk: Optional Feishu or Notion persistence can retain family data outside the chat session. <br>
Mitigation: Confirm the backend, target table or database, record scope, retention expectation, and deletion path before each read or write. <br>
Risk: Credential handling through chat could expose tokens or app secrets. <br>
Mitigation: Use platform connectors, environment variables, or local secret storage; do not request, echo, log, or write credentials in skill files. <br>
Risk: Scheduling advice could overfill a child's routine or be mistaken for professional guidance. <br>
Mitigation: Protect sleep, meals, movement, free time, and caregiver review; avoid medical, psychological, or developmental diagnosis and refer persistent concerns to qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yangchao228/skills/family-cultivation-coach) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/yangchao228) <br>
- [Project homepage from ClawHub metadata](https://github.com/yangchao228/family-baby-asistant) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, structured data, configuration, guidance] <br>
**Output Format:** [Markdown schedules, review templates, risk reminders, and optional JSON-like structured schedule blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Session-only by default; Feishu and Notion reads, writes, pushes, deletion, and retention choices require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.6.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

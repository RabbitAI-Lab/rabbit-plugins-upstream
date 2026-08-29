## Description:

SkillGuard audits third-party Agent Skill materials before installation to identify prompt injection, sensitive data exposure, dangerous commands, and supply-chain risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use SkillGuard before installing or enabling third-party skills to submit selected, redacted skill files for an API-based safety review and decide whether to pass, review, or block.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected skill materials are sent to the SkillGuard service for assessment.

Mitigation: Redact secrets, credentials, private repository data, and personal information before auditing, and limit submissions to files needed for the review.

Risk: A clean or pass result reduces risk but does not prove a third-party skill is safe.

Mitigation: Treat review, block, timeout, empty, truncated, or malformed responses as stop conditions and require human judgment before installation.

Risk: The SkillGuard API key can grant access to the paid audit service if exposed.

Mitigation: Store the key in SKILLGUARD_API_KEY, avoid pasting it into chat, and do not write it into audited source, logs, or reports.

## Reference(s):

- [SkillGuard ClawHub Listing](https://clawhub.ai/youteacher/skills/skillguard)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/skillguard/API-KEY.md)
- [Audit Workflow](https://ai-skills.open-idea.net/skill-docs/skillguard/AUDIT-WORKFLOW.md)
- [HTTP Requests and Responses](https://ai-skills.open-idea.net/skill-docs/skillguard/HTTP-REQUESTS.md)
- [Behavior, Errors, and Decision Rules](https://ai-skills.open-idea.net/skill-docs/skillguard/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SKILLGUARD_API_KEY; audit requests should include only the selected skill materials needed for assessment.]

## Skill Version(s):

1.4.1 (source: server release evidence and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

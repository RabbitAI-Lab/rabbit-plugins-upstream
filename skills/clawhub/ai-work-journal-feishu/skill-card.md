## Description:

Creates first-person AI work journal entries for troubleshooting, productivity, or exploration tasks and publishes them to a user-specified Feishu Wiki location.

This skill is ready for commercial/non-commercial use.

## Publisher:

[testman2025](https://clawhub.ai/user/testman2025)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and agent users use this skill to turn daily AI-assisted work into readable journal entries and publish them under a Feishu Wiki or cloud document parent node they specify.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create Feishu Wiki documents using the user's local Feishu session.

Mitigation: Use explicit commands that mention Feishu and review the generated journal and screenshots before publishing.

Risk: Journal content, screenshots, Wiki URLs, node tokens, or local destination configuration may contain sensitive work details.

Mitigation: Avoid saving or sharing real Wiki URLs, node tokens, passwords, App Secrets, refresh tokens, or unredacted sensitive screenshots.

Risk: Broad activation wording could make publishing intent ambiguous.

Mitigation: Confirm the destination on first use or when configuration is missing, and use the current request as authoritative when the user provides a new location.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/testman2025/skills/ai-work-journal-feishu)
- [Project Homepage](https://github.com/testman2025/ai-practice-journal-feishu)

## Skill Output:

**Output Type(s):** [Markdown, API Calls, Configuration, Guidance]

**Output Format:** [Markdown journal content plus Feishu document creation and returned document link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request screenshots and may save a local destination configuration only with user consent.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps people and legal professionals research Chinese legal disputes through comparable cases, judicial reasoning, and practical guidance with source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and legal professionals use the skill to compare Chinese court decisions, identify disputed issues, and prepare case-informed next steps. Its reports are research aids, not a substitute for professional legal review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and updates mutable third-party runner code.

Mitigation: Review or pin the runner version before running or updating it.

Risk: Legal questions are sent to the external Cue service and may contain sensitive facts.

Mitigation: Exclude unnecessary personal, privileged, or confidential details from queries.

Risk: The Cue API key is stored in a local configuration file.

Mitigation: Protect access to the key and its configuration file.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-legal-practice-cases)
- [Cue Playbook](https://cuecue.cn/playbook)
- [Cue API key management](https://cuecue.cn/api-key?src=clawhub-legal-practice-cases)
- [Cue runner dependency (GitHub)](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language Markdown report with case citations and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a saved report path and, when available, a Cue report link.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Creates, inspects, and edits Microsoft PowerPoint PPTX presentations with automated workflow support and paid enhanced layout features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent, in Chinese, to create, inspect, edit, and troubleshoot PPTX presentations. It is intended for routine automation workflows where the agent may read or write presentation files and the user reviews results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Presentation decks may contain confidential or sensitive content that the agent can read or modify.

Mitigation: Use the skill only with PPTX files the user intends the agent to access, and avoid shared or untrusted storage for confidential decks.

Risk: The skill describes command execution, file access, and possible external API use as part of automation workflows.

Mitigation: Review proposed commands and external API use before allowing execution, and run the skill with least-privilege file access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/powerpoint-pptx-cn)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with JSON status objects; file outputs may include created or modified PPTX assets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The artifact describes success/error status, execution logs, retry controls, and optional skipped steps.]

## Skill Version(s):

1.0.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Provides Markdown document processing and collaborative editing with claimed end-to-end encryption and privacy protection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, teams, and workflow automators use this skill to process, convert, extract, encrypt, and collaborate on Markdown, text, and JSON documents through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is marked suspicious because it claims strong encrypted-document privacy while requesting read/write access, command execution, online/API use, and an API key without clear boundaries.

Mitigation: Install only after the publisher clarifies what remains local, what may be sent externally, which commands may run, and when user confirmation is required.

Risk: The artifact describes handling encrypted or sensitive documents, but the evidence does not establish confidentiality boundaries.

Mitigation: Do not use confidential encrypted documents unless the publisher documents local processing, external API behavior, and data-retention expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/encrypted-docs)
- [SkillHub homepage from artifact](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON-like structured responses with optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an API key according to artifact documentation; may read, write, and execute commands through the host agent.]

## Skill Version(s):

1.0.2 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

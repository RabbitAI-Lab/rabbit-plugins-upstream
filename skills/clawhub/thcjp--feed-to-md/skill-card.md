## Description:

Converts RSS or Atom feed URLs into Markdown for agent-assisted document conversion and automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users can use this skill to turn RSS or Atom feed inputs into Markdown output during documentation, content extraction, or workflow tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read/write and command execution authority that is not clearly scoped.

Mitigation: Review the skill before installing, run it with the narrowest practical workspace and command permissions, and avoid broad file or workflow tasks until the publisher narrows the instructions.

Risk: Feed URLs, credentials, or internal network URLs may expose sensitive information when processed by a poorly scoped RSS-to-Markdown workflow.

Mitigation: Do not use sensitive feeds, credentials, internal URLs, or private network resources with this skill unless the publisher clarifies data handling and whether processing is local or remote.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feed-to-md)
- [SkillHub listing](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style status objects, with occasional inline shell commands for environment setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require agent read/write and command execution permissions depending on the requested workflow.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence; artifact frontmatter reports 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

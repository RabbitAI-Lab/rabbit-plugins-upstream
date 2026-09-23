## Description:

Guides an agent to generate short-video spoken scripts with high contrast, resonance, story structure, and personal IP positioning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to draft short-video spoken scripts for persona stories, audience pain points, and personal-brand viewpoint content. The skill also includes dLazy CLI workflow guidance that can invoke external image-generation services when those instructions are followed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags a scope mismatch: the skill is advertised as a spoken-script writer but may install or invoke the dLazy CLI for external image-generation workflows.

Mitigation: Review the skill before installation and enable it only when the dLazy CLI workflow, external API use, and hosted output URLs are intended.

Risk: The dLazy CLI workflow can send prompts and referenced media to dLazy services and can store an API key in local configuration.

Mitigation: Use organization-approved prompts and media, protect the local API key configuration, and rotate or revoke keys from the dLazy dashboard when access changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown or plain text with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs usually follow a seven-step spoken-script structure; CLI-related paths can return hosted media URLs.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

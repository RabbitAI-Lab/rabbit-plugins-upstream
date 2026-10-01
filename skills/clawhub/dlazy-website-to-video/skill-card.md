## Description:

Helps agents turn website URLs into promotional videos, social ads, or product demos using dLazy's hosted website-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers can use this skill to guide an agent through creating a website-based promo, social ad, or product demo with dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, website URLs, options, and explicitly attached files are sent to dLazy's external service.

Mitigation: Use only for intended URL-to-video tasks and review prompts and attachments before sending sensitive material.

Risk: The CLI stores an API key locally after login.

Mitigation: Protect local CLI configuration and rotate or revoke the key if exposed.

Risk: Running a third-party CLI installs or executes external package code.

Mitigation: Review the pinned npm package and its source before global installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package listed in skill metadata](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service streams responses; video creation takes place outside the agent.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release; supplied skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

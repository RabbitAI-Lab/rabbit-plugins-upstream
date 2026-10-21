## Description:

Helps create product demo and shopping-ad videos from product photos, documents, or listing links through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and marketers use this skill to request product showcase and ecommerce ad videos, including multilingual voiceovers and optional virtual hosts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected attachments may be sent to dLazy's hosted service.

Mitigation: Use the service only if its data handling is acceptable, and attach only files intended for upload.

Risk: The CLI may save an API key locally, and global installation persists the CLI.

Mitigation: Protect local credentials, rotate or revoke keys when needed, and use the pinned npx option if a global install is unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides a hosted video-generation workflow; the resulting video is produced by the dLazy service.]

## Skill Version(s):

1.0.29 (source: server release metadata; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

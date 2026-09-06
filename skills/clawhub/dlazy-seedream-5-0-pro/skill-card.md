## Description:

Professional tier of Seedream 5.0, stronger on fine detail, typography and complex composition, suited to commercial key visuals and demanding brand assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate commercial-grade images through the dLazy hosted Seedream 5.0 Pro service, including brand visuals, typography-heavy compositions, and other demanding creative assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party cloud service and sends prompts and supplied media to dLazy endpoints.

Mitigation: Review data-sharing expectations before use and avoid sending sensitive prompts or media unless the dLazy service terms and organization policy allow it.

Risk: Authentication can persist a dLazy API key in the local CLI configuration.

Mitigation: Prefer per-run DLAZY_API_KEY when a stored key is not desired, or verify and tighten permissions on ~/.dlazy/config.json after login.

Risk: Generated requests consume dLazy credits and may fail when credits are insufficient.

Mitigation: Use dry-run or account checks where appropriate and handle insufficient-balance errors before retrying generation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted image URLs, saved image files, or asynchronous task identifiers through the dLazy CLI.]

## Skill Version(s):

1.2.8 (source: server release metadata; artifact frontmatter declares 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Turns product photos, product specs, manuals, catalogs, or ecommerce listings into conversion-focused shopping ad videos with multi-language voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce operators, and marketing teams use this skill to start or continue dLazy projects that create product-focused ecommerce videos from product links, files, or prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached product files may be sent to the dLazy cloud service for video generation.

Mitigation: Avoid sending sensitive product data unless the user accepts dLazy processing; review dLazy service terms before use.

Risk: Authentication stores a dLazy API key in the user's profile configuration.

Mitigation: Use the documented login or auth command, keep the config private, and rotate or revoke the key from dLazy if exposure is suspected.

Risk: The skill invokes an external npm CLI and cloud service.

Mitigation: Use the pinned `@dlazy/cli@1.2.3` command or `npx` for on-demand execution, and review the CLI source before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent to invoke the pinned dLazy CLI template and manage project-scoped chat sessions.]

## Skill Version(s):

1.0.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

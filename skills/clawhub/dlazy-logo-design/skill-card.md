## Description:

Creates, upgrades, or evaluates logos and brand marks through dLazy's hosted logo-design agent, including brand analysis, concept refinement, multi-context previews, and transparent-background logo output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and brand teams use this skill to ask a hosted dLazy agent to create, refine, or evaluate a logo or visual identity. It is useful when an agent should produce logo-design guidance, CLI commands, and design deliverables through a project-scoped workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached reference files are sent to dLazy hosted services.

Mitigation: Send only brand assets and prompts that are appropriate for third-party processing.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Protect the local config file, prefer per-invocation environment credentials when needed, and rotate or revoke keys from the dLazy dashboard.

Risk: Broad trigger words such as logo or brand could invoke the skill unintentionally.

Mitigation: Confirm the user intends to use the dLazy logo-design workflow before sending prompts or files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, files, guidance]

**Output Format:** [Markdown or terminal text with inline shell commands and links to generated assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the pinned @dlazy/cli 1.2.3 package; attached local files are uploaded to dLazy media storage before use.]

## Skill Version(s):

1.3.10 (source: server release evidence; changelog dated 2026-09-02)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

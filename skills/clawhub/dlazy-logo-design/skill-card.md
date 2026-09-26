## Description:

Creates, upgrades, and evaluates logos and brand marks through dLazy's hosted logo-design agent, including brand-gene analysis, concept refinement, transparent-background logo delivery, and live multi-context previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask dLazy's hosted logo-design agent to create, refine, or evaluate a logo or brand identity. It is useful for logo concepts, brand kit exploration, visual identity upgrades, and multi-context presentation previews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files attached with --files are sent to dLazy's hosted service.

Mitigation: Use the skill only for content that is appropriate to share with dLazy, and avoid attaching sensitive source or private brand assets unless approved.

Risk: The dLazy CLI can store a dLazy API key in the local user configuration.

Mitigation: Use per-invocation credentials or npx when persistent installation is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or terminal text with optional shell commands and links to generated logo-design project outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference hosted dLazy project sessions and uploaded files when the user attaches local assets.]

## Skill Version(s):

1.3.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

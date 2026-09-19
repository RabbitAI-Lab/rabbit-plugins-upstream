## Description:

Creates, upgrades, or evaluates logo and brand identity concepts, including brand-gene analysis, strategy, refinement, and transparent-background logo output with multi-context previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and brand teams use this skill to create, refine, or evaluate logo and visual identity work through the dLazy hosted logo-design agent. It is suited for logo generation workflows that may include prompts and explicitly attached reference files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached files may be sent to the external dLazy service.

Mitigation: Avoid sending sensitive content unless the user's organization has approved dLazy for that data.

Risk: Authentication stores a dLazy API key in the local user configuration.

Mitigation: Use normal OS account protections for ~/.dlazy/config.json and rotate or revoke the key from the dLazy dashboard when needed.

Risk: A global CLI install persists the dLazy command on the system.

Mitigation: Use the pinned npx invocation when a non-persistent install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and terminal-oriented text from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated logo assets, previews, project identifiers, or follow-up CLI commands depending on the hosted agent response.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Generates high-fidelity vector-style assets and detailed illustrations from text prompts through the dLazy Recraft V4 Pro Vector hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request production-oriented SVG/vector-style visual assets and detailed illustrations from text prompts through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and optional media paths are sent to dLazy cloud services, and generated assets are hosted by dLazy.

Mitigation: Avoid sending confidential or regulated content unless dLazy's service terms and the user's data-handling requirements allow it.

Risk: The dLazy API key may be saved in the user's local CLI configuration.

Mitigation: Use normal secret-handling practices, prefer scoped keys where available, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: Installing the CLI globally persists a third-party executable on the system.

Mitigation: Use the pinned npx invocation when a persistent global install is not desired, and review the linked CLI source before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown instructions with CLI commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generated asset URLs are hosted by dLazy and assets can be saved locally with --save.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

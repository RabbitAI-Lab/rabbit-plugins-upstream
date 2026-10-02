## Description:

Uses the dLazy CLI to generate text, reasoning, and code from prompts, with optional image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask an agent to generate or refine text and code, optionally using images or videos as input through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI stores or accepts a dLazy API key.

Mitigation: Protect the key and rotate or revoke it if exposed.

Risk: Prompts are sent to dLazy, and supplied local images or videos are uploaded to its service.

Mitigation: Send only prompts and media approved for third-party processing.

Risk: Installing the third-party CLI globally leaves a persistent executable on the system.

Mitigation: Review the pinned package and source before installation, or use the on-demand npx option.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI source referenced in skill metadata (not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [CLI JSON response containing generated content or an asynchronous task identifier]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include hosted output URLs; asynchronous jobs can be polled.]

## Skill Version(s):

1.2.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

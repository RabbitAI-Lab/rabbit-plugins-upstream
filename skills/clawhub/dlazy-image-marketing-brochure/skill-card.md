## Description:

A workflow skill for designing marketing brochures, from requirements gathering and layout planning through confirmed folded and lifestyle mock-up delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative teams use this skill to plan brochure structure, generate layout-first marketing brochure artwork, and produce folded or lifestyle mock-ups after explicit layout approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and any referenced media files to dLazy's external CLI and cloud API.

Mitigation: Use it only when external processing is acceptable, avoid submitting sensitive media or confidential prompt content, and review dLazy's service terms before use.

Risk: API keys may be stored in the local dLazy CLI configuration when using the login or auth setup flow.

Mitigation: Use the per-run DLAZY_API_KEY option when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The artifact contains a CLI version mismatch between the install command and prose documentation.

Mitigation: Review the @dlazy/cli package source and intended version before installation, and prefer the pinned command shown in the release metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces brochure planning prompts, layout confirmation requests, and links to generated image outputs from dLazy-hosted media.]

## Skill Version(s):

1.3.21 (source: server release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

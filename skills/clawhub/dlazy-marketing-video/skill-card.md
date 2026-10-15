## Description:

Creates promotional and ecommerce videos from product details, listings, or campaign briefs through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and sellers use this skill to create promotional or shopping videos from product materials and listings for social media and advertising campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product materials, and selected attachments are sent to dLazy's hosted service.

Mitigation: Send only materials approved for that service; avoid confidential attachments unless intended.

Risk: Saved projects can retain context across unrelated work.

Mitigation: Start a fresh project for unrelated tasks and rotate or revoke the API key when access should end.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text and Markdown with CLI commands and links to generated videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation runs through dLazy's hosted service and can continue in a saved project.]

## Skill Version(s):

1.0.25 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

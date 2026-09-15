## Description:

Generates images by selecting an appropriate dLazy CLI image model based on the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users use this skill to route image-generation prompts to dLazy CLI models and receive generated image results through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use requires trusting the external dLazy npm CLI.

Mitigation: Prefer the pinned npx invocation or another non-global install, and review the CLI package before use.

Risk: Prompts and selected media files are sent to dLazy's hosted service.

Mitigation: Avoid passing sensitive prompts or local media files unless the user accepts that data transfer.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Use a revocable key, restrict access to the workstation account, and rotate the key if compromise is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [ClawHub publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI project link from release metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline bash commands and dLazy CLI output references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted generated-image URLs and JSON envelopes from the dLazy CLI.]

## Skill Version(s):

1.3.17 (source: ClawHub release evidence, created 2026-09-14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

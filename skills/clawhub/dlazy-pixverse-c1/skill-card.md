## Description:

Generates PixVerse C1 videos from text prompts, reference images, or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short PixVerse C1 videos from text prompts, reference images, or first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media inputs are sent to dLazy's hosted service.

Mitigation: Upload only media you are comfortable sharing with dLazy, and review prompts and inputs for sensitive content.

Risk: The API key is saved in the local dLazy CLI configuration.

Mitigation: Protect the saved key and rotate or revoke it if exposed.

Risk: Video generation can incur usage costs.

Mitigation: Use the documented --dry-run option to preview the generation payload and estimated cost.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, JSON result with output URLs, Shell commands]

**Output Format:** [Generated video asset and JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-based generation with optional reference media; clips up to 15 seconds; asynchronous generation is supported.]

## Skill Version(s):

1.2.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Generates videos from text prompts and optional image, video, audio, or first-and-last-frame references through the dLazy Seedance 2.0 CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate videos from prompts and optional media references, with control over duration, aspect ratio, and resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI may store a dLazy API key locally.

Mitigation: Confirm you trust the CLI and service before installing, and protect or revoke the API key as needed.

Risk: Prompts and explicitly supplied media are sent to dLazy-hosted endpoints.

Mitigation: Only submit prompts and media you are comfortable sharing with the service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Video asset URLs]

**Output Format:** [JSON result with hosted media URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets can optionally be saved locally; asynchronous tasks may require polling.]

## Skill Version(s):

1.3.20 (source: ClawHub release metadata; artifact frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Generates videos with Tongyi Wanxiang 2.7 from text prompts, first and last frames, and reference images or videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creators use the skill to generate videos from prompts, reference media, or specified first and last frames through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service, and generated assets are hosted there.

Mitigation: Submit only prompts and media you are comfortable uploading.

Risk: The CLI can save an API key locally, and video generation can incur service costs.

Mitigation: Protect the local configuration, use --dry-run to review a cost estimate, and rotate or revoke keys when needed.

## Reference(s):

- [dLazy CLI project on GitHub](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video assets, JSON]

**Output Format:** [JSON response with generated media URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted by dLazy; the CLI can optionally save an asset locally.]

## Skill Version(s):

1.3.36 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

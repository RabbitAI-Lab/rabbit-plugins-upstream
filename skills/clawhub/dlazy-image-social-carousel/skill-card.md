## Description:

A structured workflow skill dedicated to social-media carousel design. The core method is 'decide intent first, then execute,' using a 'single-confirmation + cover-first' two-phase flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and social-media marketers use this skill to plan platform-specific carousel slides, confirm the direction, and guide cover-first image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports differing CLI installation versions and incomplete scan evidence; the workflow also requires CLI authentication.

Mitigation: Review the current CLI installation and authentication instructions before installing, and use a version and login method you trust.

Risk: The documented workflow sends prompts to dLazy's hosted API and may upload local media for processing.

Mitigation: Avoid sending sensitive prompts or media, and use an API key that can be rotated or revoked.

## Reference(s):

- [dLazy CLI source repository (referenced by skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown with tables and structured carousel plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Platform-specific slide roles, headlines, subheadlines, references, and a cover-first generation workflow.]

## Skill Version(s):

1.3.39 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

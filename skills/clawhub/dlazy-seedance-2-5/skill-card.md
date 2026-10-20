## Description:

Helps agents generate short videos with Seedance 2.5 using text prompts, optional image, video, or audio references, and first/last-frame controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short video clips from text and optional media references through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external dLazy CLI stores an API key locally for cloud requests.

Mitigation: Review the CLI before installation, protect its local configuration, and rotate or revoke the key if needed.

Risk: Prompts and referenced local media are sent to dLazy cloud endpoints.

Mitigation: Only submit content you are authorized to share with the service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI repository (listed in skill metadata; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown instructions and JSON generation results with media URLs or asynchronous task IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local download of generated media; generation requires a dLazy account and API key.]

## Skill Version(s):

1.2.28 (source: ClawHub release metadata; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

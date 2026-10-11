## Description:

Generates short MiniMax Hailuo videos from prompts, frame transitions, or reference media through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short videos from text prompts, start and end frames, or reference images, videos, and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party CLI requires trusting its package and account model.

Mitigation: Review the package before installing; use the pinned on-demand CLI invocation if a persistent global binary is unnecessary.

Risk: Authentication may save an API key in local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials if local storage is undesirable.

Risk: Local media supplied for generation is uploaded to the hosted service.

Mitigation: Only pass files you are comfortable uploading to dLazy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI repository (declared in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Text instructions and CLI JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs or asynchronous task IDs; optional local download.]

## Skill Version(s):

1.2.24 (source: ClawHub release metadata; artifact frontmatter and pinned CLI: 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Adapts web novels into Chinese webtoon plot breakdowns and episode scripts, with optional dLazy image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and creators use the skill to turn web novels into structured plot breakdowns and episode scripts for webtoon adaptation. It can also guide user-confirmed image generation through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy services for processing.

Mitigation: Send only content the user has approved for cloud processing.

Risk: Logging in stores the dLazy API key in the local CLI configuration.

Mitigation: Protect access to the local configuration and rotate or revoke the key if it is exposed.

Risk: The artifact contains conflicting CLI version references.

Mitigation: Resolve the version discrepancy and verify the intended package version before installing; the security guidance points to the explicit 1.2.3 install instructions.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese Markdown with structured plot breakdowns and episode scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses 【剧情n】 plot markers and visual-description markers in scripts; optional generated images are returned as URLs.]

## Skill Version(s):

1.3.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

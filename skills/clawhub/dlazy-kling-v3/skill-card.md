## Description:

Helps generate Kling v3 videos from text prompts or reference images through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate videos from text prompts or reference images with Kling v3 through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Protect local credentials; use a per-invocation key where appropriate and rotate or revoke exposed keys.

Risk: Prompts and supplied media are sent to dLazy-hosted services.

Mitigation: Review prompts and media before submission and avoid uploading sensitive material without approval.

Risk: Installing the CLI introduces third-party package supply-chain exposure.

Mitigation: Review the pinned npm package and its source before installation.

Risk: Insufficient balance messages may direct users to a recharge page.

Mitigation: Treat recharge as a deliberate account action; confirm costs and the destination before proceeding.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown instructions and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain a hosted asset URL or an asynchronous task ID; an optional command can save the asset locally.]

## Skill Version(s):

1.3.26 (source: server release metadata; skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

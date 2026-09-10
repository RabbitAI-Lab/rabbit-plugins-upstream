## Description:

Generates Seedance 2.0 Fast videos from text and optional image, video, audio, or first/last-frame references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to ask an agent to run the dLazy CLI for fast Seedance 2.0 video generation with text prompts and optional multimodal references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party npm CLI and dLazy-hosted API endpoints.

Mitigation: Install only if you trust the dLazy publisher and package; prefer the pinned on-demand npx invocation when a persistent global binary is unnecessary.

Risk: Prompts, parameters, and referenced local media may be sent to dLazy API and storage services.

Mitigation: Use a revocable dLazy API key and pass only media files that are appropriate to upload to dLazy.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands; the CLI returns JSON containing hosted media URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may upload referenced local media files to dLazy-hosted storage.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

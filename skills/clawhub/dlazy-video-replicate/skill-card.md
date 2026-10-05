## Description:

Guides an agent to extract a video's first frame and audio and generate a Seedance 2.0 replication prompt and media bundle using dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to prepare a video-replication bundle from a source video, including a first frame, audio, and a generated description for Seedance 2.0.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos, audio, images, prompts, and parameters supplied to the CLI may be uploaded to dLazy-hosted services.

Mitigation: Only submit media and prompts you are authorized to share; review sensitive content before invoking the service.

Risk: Use requires a dLazy account and API key; a global CLI installation persists on the host.

Mitigation: Use npx instead of a global install if preferred, protect the API key, and rotate or revoke it in the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI repository (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown instructions and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses can include hosted media URLs or an asynchronous task ID.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

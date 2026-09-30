## Description:

Extracts a source video's first frame and audio, analyzes the video to produce a prompt, and returns a Seedance 2.0 replication bundle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to analyze a reference video and prepare a first-frame, audio, and video bundle for Seedance 2.0 replication through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI.

Mitigation: Review the CLI before installing; use the documented pinned npx command if a persistent global install is undesirable.

Risk: An API key may be saved in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if it is exposed.

Risk: Media files supplied to the command are uploaded to dLazy's hosted service.

Mitigation: Avoid submitting private videos unless dLazy's terms and account controls meet your requirements.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Markdown guidance and JSON results with generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async requests may return a task ID instead of completed outputs.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; bundled skill frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

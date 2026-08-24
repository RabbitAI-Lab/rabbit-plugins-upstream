## Description:

Detects whether image, video, or audio media is AI-generated, including visual deepfake signals and likely generator attribution with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run dLazy media detection on approved images, videos, or audio and report AI-generation, deepfake, or generator-attribution confidence results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media can be uploaded to external dLazy services, which may expose private, confidential, or biometric content.

Mitigation: Use only public URLs or explicitly approved local files, and avoid sensitive media unless permission and the service privacy terms have been reviewed.

Risk: Broad trigger wording can lead to accidental use on media the user did not intend to send to external services.

Mitigation: Confirm the media source and user consent before running detection, especially when the input is a local file.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON results with human-readable text summaries and concise command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; accepts exactly one image, video, or audio input per invocation; local files may be uploaded to dLazy media storage.]

## Skill Version(s):

1.0.8 (source: server release evidence; artifact frontmatter lists 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

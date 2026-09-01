## Description:

Detects whether images, videos, or audio are AI-generated, including visual deepfakes and likely generator attribution, and returns confidence scores for threshold-based decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to check media for AI generation, visual deepfake signals, audio AI-generation signals, and likely generator attribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media files selected for analysis may be uploaded to dLazy's hosted service for processing.

Mitigation: Confirm the media is intended for AI or deepfake detection, prefer public URLs or non-sensitive samples when practical, and avoid submitting private or sensitive files unless that hosted processing is acceptable.

Risk: Authentication stores a dLazy API key in the local CLI configuration when using login or manual auth setup.

Mitigation: Use the documented dLazy authentication flow only in trusted environments and manage the saved API key according to the user's credential-handling practices.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-detect)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [JSON detection results with human-readable text or Markdown guidance and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The detector accepts exactly one image, video, or audio input per invocation and does not support text analysis.]

## Skill Version(s):

1.0.10 (source: server release evidence; artifact frontmatter reports 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

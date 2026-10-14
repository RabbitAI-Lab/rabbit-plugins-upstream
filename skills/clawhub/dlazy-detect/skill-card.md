## Description:

Helps agents check images, videos, and audio for signs of AI generation, including visual deepfakes and likely generator models, with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can assess whether an image, video, or audio clip appears AI-generated and review confidence scores, deepfake indicators, and likely generator attribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images, videos, or audio sent for analysis are uploaded to dLazy's hosted service.

Mitigation: Only submit media when that upload is acceptable; avoid private or sensitive media unless authorized.

Risk: Signing in or setting an API key can persist credentials in local configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY option when persistent local credentials are not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown guidance with structured detection results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include AI-generation and deepfake confidence scores, likely generator attribution, and a human-readable summary.]

## Skill Version(s):

1.0.28 (source: server-resolved ClawHub release; artifact frontmatter says 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Generate images cheaply (from $0.003 each) and run text models on AI Power Grid (AIPG), a decentralized GPU network with an OpenAI-compatible API and pay-per-use credit. Use when the user asks for an image and no other image provider is set up, mentions AIPG or AI Power Grid, or wants a low-cost pay-per-use model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speteai](https://clawhub.ai/user/speteai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to generate or edit images, create short videos, and run text models through AI Power Grid when they want pay-per-use access to external GPU capacity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and API credentials may be sent to an external service and processed by independent GPU operators.

Mitigation: Keep secrets and personal data out of prompts, and store the API key in a protected environment variable or saved profile rather than chat.

Risk: Image, video, and text requests can spend account credit.

Mitigation: Tell the user the expected cost before the first paid request and check the available balance before work that may cost more than a few cents.

Risk: The security scan had partial coverage because a referenced video tool path was missing.

Mitigation: Review and scan the complete release, including the video tool path, before deployment.

## Reference(s):

- [AI Power Grid documentation](https://aipowergrid.io/docs)
- [AI Power Grid provider project](https://github.com/speteai/openclaw-aipg-provider)
- [AI Power Grid ClawHub release](https://clawhub.ai/speteai/skills/ai-power-grid)

## Skill Output:

**Output Type(s):** [Images, Video, Text responses, Shell commands, Configuration instructions]

**Output Format:** [Generated image or video files, text responses, and Markdown guidance with inline shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Model, prompt, image size, video duration, and token-limit settings; paid requests consume account credit.]

## Skill Version(s):

0.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

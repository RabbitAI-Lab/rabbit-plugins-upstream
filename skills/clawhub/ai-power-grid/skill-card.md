## Description:

Generate images cheaply (from $0.003 each) and run text models on AI Power Grid (AIPG), a decentralized GPU network with an OpenAI-compatible API and pay-per-use credit. Use when the user asks for an image and no other image provider is set up, mentions AIPG / AI Power Grid / the grid, or wants a low-cost pay-per-use model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speteai](https://clawhub.ai/user/speteai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw agents use this skill to generate or edit images, create short videos, and get text responses through AI Power Grid. It is intended for image requests when no other image provider is configured, or when a user asks for AIPG or a low-cost pay-per-use model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, requests, and API credentials may be processed in plain text by independent GPU operators.

Mitigation: Do not send secrets, credentials, or personal data; keep sensitive details out of prompts and store the API key in the environment or OpenClaw's credential store.

Risk: Paid requests spend account credit, and wallet funding cannot be withdrawn.

Mitigation: Tell the user the approximate cost before the first paid request, check the available balance, and only submit wallet funding with explicit approval for the amount.

Risk: The security analysis was partial and reported two unresolved local references.

Mitigation: Review the referenced materials and the skill's behavior before use.

## Reference(s):

- [AI Power Grid skill documentation](https://aipowergrid.io/.well-known/skills/grid/SKILL.md)
- [OpenClaw AIPG provider repository](https://github.com/speteai/openclaw-aipg-provider)

## Skill Output:

**Output Type(s):** [Images, Video, Text, API Calls, Shell commands, Configuration instructions]

**Output Format:** [Generated images and video, text responses, and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation supports up to four images per call; video generation supports up to 26 seconds. Availability and model options depend on online workers and account credit.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

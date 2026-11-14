## Description:

Generate images cheaply (from $0.003 each) and run text models on AI Power Grid (AIPG), a decentralized GPU network with an OpenAI-compatible API and pay-per-use credit. Use when the user asks for an image and no other image provider is set up, mentions AIPG or AI Power Grid, or wants a low-cost pay-per-use model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speteai](https://clawhub.ai/user/speteai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users use the skill to request image generation or editing, video generation, and text-model responses through AI Power Grid, including when no other image provider is configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests are sent to an external service and may be processed by independent operators; usage can incur charges.

Mitigation: Keep secrets, credentials, and personal data out of prompts, and check the price and available credit before paid requests.

Risk: The security review is partial and does not establish what an unresolved reference associated with video generation points to.

Mitigation: Resolve and review that reference before relying on the associated video-generation guidance.

## Reference(s):

- [AI Power Grid documentation](https://aipowergrid.io/docs)
- [AIPG provider project](https://github.com/speteai/openclaw-aipg-provider)

## Skill Output:

**Output Type(s):** [Images, Video, Text, Guidance]

**Output Format:** [Generated image or video files, text responses, and Markdown guidance with shell and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requests use pay-per-use credit and may incur charges.]

## Skill Version(s):

0.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Generate video from text, reference media, or first and last frames with MiniMax H3 through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate MiniMax H3 videos through RunAPI for one-off CLI tasks, manual tests, or application integration through SDKs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated prompts and referenced media may be sent to RunAPI when the skill is used.

Mitigation: Use the skill only for intended RunAPI/MiniMax H3 workflows and review RunAPI pricing, retention, and terms before production use.

Risk: API keys can be exposed if copied into source files or logs.

Mitigation: Keep keys in RUNAPI_API_KEY or saved RunAPI CLI configuration and do not commit secrets.

Risk: Generated file URLs are temporary and may expire before downstream users retrieve them.

Mitigation: Download generated files into durable storage within the retention window.

## Reference(s):

- [MiniMax H3 model overview](https://runapi.ai/models/minimax-h3)
- [MiniMax H3 documentation](https://runapi.ai/models/minimax-h3.md)
- [MiniMax provider comparison](https://runapi.ai/providers/minimax.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI publisher profile](https://clawhub.ai/user/runapi-ai)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-minimax-h3)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands, SDK package names, request guidance, and security notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide use of the runapi CLI or language SDKs; generated media URLs are temporary and should be downloaded into durable storage.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

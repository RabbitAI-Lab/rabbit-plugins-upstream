## Description:

Call the MiniMax text API (MiniMax-M3 through MiniMax-M2) through RunAPI using OpenAI-compatible Chat Completions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call MiniMax text chat models through RunAPI using OpenAI-compatible Chat Completions, including streaming and compatibility-client guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chat content and prompts are sent to RunAPI/MiniMax.

Mitigation: Use only data approved for that provider, and avoid secrets, regulated data, or private customer content unless organizational approval and data handling terms are in place.

## Reference(s):

- [MiniMax compatibility protocols](references/compatibility-protocols.md)
- [RunAPI MiniMax model documentation](https://runapi.ai/models/minimax.md)
- [RunAPI MiniMax provider documentation](https://runapi.ai/providers/minimax.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI MiniMax homepage](https://runapi.ai/models/minimax)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-minimax)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Python code examples and environment-variable configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes OpenAI-compatible request guidance, streaming verification, retry boundaries, and compatibility protocol notes.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

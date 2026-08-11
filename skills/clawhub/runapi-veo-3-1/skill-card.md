## Description:

Generate and edit video with Veo 3 through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, edit, extend, and upscale Veo 3 videos through RunAPI. It supports one-off CLI generation and SDK-oriented application integration guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, input files, and media requests may be sent to RunAPI, and usage may incur provider costs.

Mitigation: Install and use the skill only when RunAPI/Veo 3.1 is intended, and use an API key or saved CLI login deliberately.

Risk: Generated RunAPI file URLs are temporary and should not be treated as long-term assets.

Mitigation: Download generated media and store it in durable storage within 7 days.

## Reference(s):

- [RunAPI Veo 3.1 model overview](https://runapi.ai/models/veo-3.1)
- [RunAPI Veo 3.1 documentation](https://runapi.ai/models/veo-3.1.md)
- [Google provider comparison](https://runapi.ai/providers/google.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)
- [Veo 3.1 variant](https://runapi.ai/models/veo-3.1/veo-3.1.md)
- [Veo 3 fast variant](https://runapi.ai/models/veo-3.1/fast.md)
- [Veo 3 Lite variant](https://runapi.ai/models/veo-3.1/lite.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may result in RunAPI API calls that send prompts, input files, and media requests to RunAPI.]

## Skill Version(s):

0.2.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

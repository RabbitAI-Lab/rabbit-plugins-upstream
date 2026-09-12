## Description:

Creates Gemini Omni voice resources, character resources, and Flash Preview or multimodal text-to-video tasks through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create or manage Gemini Omni voices, character resources, and video generation tasks through RunAPI while validating request contracts and media deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an external RunAPI CLI installed from a Homebrew tap that is not pinned in the artifact.

Mitigation: Confirm the RunAPI CLI publisher and tap before installation and inspect the installed command contract before submitting requests.

Risk: Generated media requests may upload local files and incur service costs.

Mitigation: Review local media paths before submission, use a scoped RunAPI API key where possible, and submit paid tasks only with user authorization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-gemini-omni)
- [RunAPI Gemini Omni model overview](https://runapi.ai/models/gemini-omni)
- [Gemini Omni documentation](https://runapi.ai/models/gemini-omni.md)
- [RunAPI Google provider overview](https://runapi.ai/providers/google.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Gemini Omni SDK integration](https://github.com/runapi-ai/gemini-omni-sdk)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown with inline shell commands, JSON request examples, and integration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to create request.json, task.json, result files, and downloaded audio or video media when the user asks for generated deliverables.]

## Skill Version(s):

0.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

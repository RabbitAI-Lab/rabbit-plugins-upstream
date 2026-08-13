## Description:

Generate and edit images with GPT Image 2 through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create, edit, or transform images with GPT Image 2 through RunAPI, using the CLI for one-off tasks and SDK references for application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit paid RunAPI image-generation tasks using stored or provided authentication.

Mitigation: Confirm RunAPI billing and authentication expectations before installation or execution; the skill checks authentication before submitting work.

Risk: A replacement task could create duplicate cost or conflicting evidence after a timeout or transport failure.

Mitigation: The skill preserves the created task ID, waits on the same task, and avoids replacement submissions without user authorization.

Risk: Generated media links may be missing, empty, or have an unexpected file type.

Mitigation: The skill downloads each requested media deliverable and checks that every file is non-empty and matches the expected image MIME type.

## Reference(s):

- [RunAPI GPT Image 2 Homepage](https://runapi.ai/models/gpt-image-2)
- [Model overview, pricing, and rate limits](https://runapi.ai/models/gpt-image-2.md)
- [Provider overview](https://runapi.ai/providers/openai.md)
- [Full model catalog](https://runapi.ai/models.md)
- [SDK integration](https://github.com/runapi-ai/gpt-image-2-sdk)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-gpt-image-2)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, files]

**Output Format:** [Markdown guidance with shell commands, JSON request and response files, and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves task evidence, waits on the submitted task by default, and verifies downloaded image files before reporting completion.]

## Skill Version(s):

0.2.9 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Uses the Flyelep AI Tool API to remove image backgrounds for one or more public image URLs and return matted image URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to remove backgrounds from product, subject, or other user-provided images by collecting public image URLs and a Flyelep API key, then presenting the returned transparent-background image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image URLs and the Flyelep API key are sent to Flyelep during execution.

Mitigation: Use non-sensitive public image URLs, provide the API key only at runtime, and avoid saving the key in files or chat history.

Risk: Temporary payload files may contain submitted image URLs when the Windows/PowerShell flow is used.

Mitigation: Create temporary payload files only when needed and delete them after the API response is received.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-ai-image-matting)
- [Flyelep AI image matting API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/aiImageMatting)
- [Flyelep controlboard](https://www.flyelep.cn/controlboard)

## Skill Output:

**Output Type(s):** [Text, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown guidance with JSON payloads, shell command examples, and returned image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided image URLs and a Flyelep secretKey; Windows/PowerShell usage may create a temporary JSON payload file that should be deleted after the API call.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

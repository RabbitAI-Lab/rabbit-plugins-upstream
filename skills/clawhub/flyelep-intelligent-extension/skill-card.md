## Description:

Uses the Flyelep AI Tool API to intelligently extend one or more user-provided images to a requested target aspect ratio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and creative tooling agents use this skill to collect image URLs and a target ratio, call Flyelep's intelligent-extension API, and return the resulting image URLs in input order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided image URLs and the Flyelep API key are sent to Flyelep when the skill is run.

Mitigation: Use only images appropriate for the Flyelep service, provide the API key at runtime, and do not store the key in skill files, examples, repositories, or persistent configuration.

Risk: A temporary payload_temp.json file may contain request data when used for Windows or PowerShell execution.

Mitigation: Create the payload as UTF-8 without BOM only when needed, use it for the API request, and remove it after the response is handled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-intelligent-extension)
- [Flyelep intelligent-extension API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/intelligentExtension)
- [Flyelep controlboard](https://www.flyelep.cn/controlboard)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with JSON payload examples and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns generated image URLs from the API response; temporary payload files should be removed after use.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

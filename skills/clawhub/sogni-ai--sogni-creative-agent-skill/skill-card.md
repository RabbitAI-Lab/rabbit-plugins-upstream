## Description:

Helps agents generate and edit images, videos, music, and other creative media through Sogni AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

Creators and developers use this skill with an agent to create or edit images, video, audio, and music, and to manage related Sogni creative workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI accesses a Sogni API key and persistent Sogni configuration.

Mitigation: Provide credentials only when you trust the integration and protect the local credentials file.

Risk: Hosted workflows may transmit selected local media or incur charges.

Mitigation: Use direct CLI mode for media that must stay local and review hosted workflow costs before bypassing cost confirmation.

Risk: Optional global installs or self-updates change the installed package.

Mitigation: Approve installs or updates only when you intend to refresh the package.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Sogni AI](https://sogni.ai)
- [Sogni model catalog](https://api.sogni.ai/v1/model-catalog)
- [Model guide](references/models.md)
- [Hosted API guide](references/hosted-api.md)

## Skill Output:

**Output Type(s):** [Images, Videos, Audio, JSON, Guidance]

**Output Format:** [Media files and text or structured JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include saved file paths, URLs, status, and error details.]

## Skill Version(s):

3.56.1 (source: release evidence, skill metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

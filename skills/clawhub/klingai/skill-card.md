## Description:

Calls Kling AI for video generation, image generation, subject management, and account quota inquiry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[klingai-dev](https://clawhub.ai/user/klingai-dev)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn Kling AI generation, subject-management, and quota requests into validated CLI actions. It helps agents choose the correct video, image, element, or account workflow before submitting billable Kling API tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to Kling AI for generation and subject workflows.

Mitigation: Submit only prompts and media that are appropriate to share with Kling AI, and confirm ambiguous generation intent before starting billable tasks.

Risk: Kling API keys may be persisted under the Kling storage root when bind, import, or configure flows are used.

Mitigation: Prefer session-only KLING_API_KEY for non-persistent use, or protect and periodically review the local Kling credentials storage.

Risk: Subject deletion is explicit but not separately confirmed by the skill.

Mitigation: Review delete commands and subject identifiers carefully before execution.

Risk: Generated assets may be removed by the platform after a retention period.

Mitigation: Download and retain needed outputs locally after successful generation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/klingai-dev/skills/klingai)
- [Kling AI API Documentation](https://klingai.com/document-api/)
- [Kling AI Docs Index](https://klingai.com/document-api/llms.txt)
- [Kling API Authentication](https://klingai.com/document-api/api/get-started/authentication.md)
- [Video Capability Map](https://klingai.com/document-api/guides/capability-map/video.md)
- [Image Capability Map](https://klingai.com/document-api/guides/capability-map/image.md)
- [Kling Elements API](https://klingai.com/document-api/api/video/3-0-omni/elements.md)
- [Account Usage API](https://klingai.com/document-api/api/assets/account-usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell commands; CLI runs print task status and local output paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media can be downloaded to the selected output directory; account and subject commands may print status, quota, or task identifiers.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

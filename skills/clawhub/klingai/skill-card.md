## Description:

Official Kling AI Skill. Call Kling AI for video generation, image generation, subject management, and account quota inquiry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[klingai-dev](https://clawhub.ai/user/klingai-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to route natural-language Kling AI requests into Node.js commands for video generation, image generation, subject management, account quota checks, and credential setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, referenced media, subject data, and account requests are sent to Kling AI.

Mitigation: Install and use the skill only when that data transfer is acceptable for the user's content and account.

Risk: The skill can store an API key under ~/.config/kling or KLING_STORAGE_ROOT.

Mitigation: Treat stored credentials as sensitive, avoid importing credentials on shared machines, and prefer session-only KLING_API_KEY where appropriate.

Risk: Generation requests can be billable.

Mitigation: Confirm user intent before submitting generation jobs, especially when the request is ambiguous.

Risk: Subject delete requests can remove Kling AI subject resources.

Mitigation: Double-check the target subject before running a delete action.

## Reference(s):

- [Kling AI document API homepage](https://klingai.com/document-api/)
- [Kling AI API reference](reference.md)
- [Kling AI authentication](https://klingai.com/document-api/api/get-started/authentication.md)
- [Docs index](https://klingai.com/document-api/llms.txt)
- [Video capability map](https://klingai.com/document-api/guides/capability-map/video.md)
- [Image capability map](https://klingai.com/document-api/guides/capability-map/image.md)
- [Elements](https://klingai.com/document-api/api/video/3-0-omni/elements.md)
- [Account costs](https://klingai.com/document-api/api/assets/account-usage.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown with inline Node.js command examples and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Kling task IDs, downloaded media file paths, API status messages, and account quota summaries.]

## Skill Version(s):

2.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

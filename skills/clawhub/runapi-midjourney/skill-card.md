## Description:

Generate and edit images, create or extend video from images, derive or shorten prompt suggestions, and look up seeds with Midjourney through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate and edit Midjourney images, create image-based video, retrieve seeds, and prepare RunAPI CLI or SDK requests for one-off work and application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media paths included in requests may be sent to RunAPI or Midjourney.

Mitigation: Avoid private files or sensitive prompt content unless they are intended inputs, and review request JSON before submission.

Risk: Midjourney operations may consume paid credits.

Mitigation: Submit each request only once, verify task creation before retrying, and require user authorization before any replacement paid request.

Risk: The skill depends on the external RunAPI CLI and authentication state.

Mitigation: Confirm the installed RunAPI CLI is trusted and authenticated before executing model operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-midjourney)
- [RunAPI Midjourney model overview](https://runapi.ai/models/midjourney)
- [RunAPI Midjourney model documentation](https://runapi.ai/models/midjourney.md)
- [RunAPI Midjourney provider documentation](https://runapi.ai/providers/midjourney.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Midjourney SDK](https://github.com/runapi-ai/midjourney-sdk)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to produce request JSON, task identifiers, response files, downloaded media files, and SDK integration code.]

## Skill Version(s):

0.3.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

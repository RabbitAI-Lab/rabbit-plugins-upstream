## Description:

Capture a full-page PNG screenshot of a public URL through Scavio and return the image inline as a base64 data:image/png URI with capture metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to capture public web pages as full-page PNG screenshots for previews, reports, visual testing, OCR, or vision-model inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target webpage URLs are sent to a third-party screenshot API.

Mitigation: Avoid private, sensitive, or internal URLs unless the provider has been verified and capture is authorized.

Risk: The skill requires a Scavio API key and successful captures may consume billing credits.

Mitigation: Use a properly scoped secret, keep it out of source control, and confirm the selected capture tier before running costly captures.

Risk: Returned image data can be large because screenshots are provided inline as base64 PNG data URIs.

Mitigation: Decode large screenshot payloads to files before passing them into prompts or downstream tools.

## Reference(s):

- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=website-screenshot-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=website-screenshot-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/website-screenshot-api)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON examples and Python or curl code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and returns screenshot data as an inline base64 PNG data URI with URL, image format, mode, and image byte metadata.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

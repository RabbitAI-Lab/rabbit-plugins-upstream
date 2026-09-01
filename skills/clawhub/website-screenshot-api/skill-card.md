## Description:

Captures a full-page PNG screenshot of a public URL through Scavio and returns it as an inline base64 data:image/png URI with URL, format, capture mode, and image size metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to capture public web pages as full-page PNG screenshots for reports, previews, visual comparisons, OCR, or vision-model inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested URLs are sent to Scavio for screenshot capture and may involve third-party processing.

Mitigation: Avoid private, internal, token-bearing, or sensitive URLs unless that third-party processing is acceptable.

Risk: Screenshot captures may consume Scavio credits, and ultra mode costs more than normal or advanced mode.

Mitigation: Start with normal mode and use higher tiers only when the returned image is blank or incomplete.

Risk: Returned image data URIs can be large.

Mitigation: Decode large base64 images to files instead of pasting them into prompts or logs.

## Reference(s):

- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=website-screenshot-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=website-screenshot-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/website-screenshot-api)

## Skill Output:

**Output Type(s):** [API Calls, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Python, bash, and JSON examples; API responses include base64 PNG data URIs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; sends requested URLs to Scavio; successful captures consume Scavio credits.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

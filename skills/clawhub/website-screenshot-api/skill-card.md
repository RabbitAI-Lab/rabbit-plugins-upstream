## Description:

Capture a full-page PNG screenshot of any public URL, returned inline as a base64 data:image/png URI ready to drop into an <img> tag.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent builders use this skill to capture full-page website screenshots for previews, reports, visual comparisons, OCR, and vision-model inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends target URLs to a third-party screenshot provider.

Mitigation: Use it only for public or approved URLs and avoid submitting private, sensitive, or internal pages.

Risk: SCAVIO_API_KEY is required for API access.

Mitigation: Store the key as a secret, pass it through the environment, and avoid committing or pasting it into shared logs.

Risk: Successful captures consume credits, with ultra mode costing more than normal or advanced mode.

Mitigation: Start with normal mode and use advanced or ultra only when the returned image is blank or incomplete.

Risk: Returned screenshots are large base64 PNG data URIs.

Mitigation: Decode the image to a file when practical rather than pasting the full base64 payload into prompts or documents.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/website-screenshot-api)
- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=website-screenshot-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=website-screenshot-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Image data, Shell commands, Code]

**Output Format:** [JSON response containing URL, image_format, mode, image_bytes, and a base64 data:image/png URI; guidance may include Markdown with Python or curl examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Successful captures consume credits, with normal and advanced modes at 1 credit and ultra mode at 5 credits.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

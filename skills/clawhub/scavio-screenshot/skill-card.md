## Description:

Capture a full-page PNG screenshot of any public URL, returned inline as a base64 data:image/png URI ready to drop into an <img> tag.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to capture full-page screenshots of public web pages for previews, reports, visual checks, OCR input, or downstream vision workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested public URLs and rendered page contents are sent to Scavio for screenshot generation.

Mitigation: Use only public pages and avoid private, authenticated, internal, tokenized, or secret-bearing links.

Risk: Advanced and ultra capture modes can increase credit usage.

Mitigation: Start with normal mode and escalate only when the returned screenshot is blank or incomplete.

Risk: The returned image data URI can be large.

Mitigation: Decode large base64 PNG data to a file instead of pasting it into prompts or chat messages.

## Reference(s):

- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=website-screenshot-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=website-screenshot-api)
- [Scavio Screenshot API on ClawHub](https://clawhub.ai/scavio-ai/skills/scavio-screenshot)

## Skill Output:

**Output Type(s):** [API calls, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python, curl, JSON examples, and API responses containing screenshot metadata plus a base64 PNG data URI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; normal and advanced captures cost 1 credit, while ultra captures cost 5 credits.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

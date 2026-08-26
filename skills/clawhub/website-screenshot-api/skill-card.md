## Description:

Capture a full-page PNG screenshot of any public URL, returned inline as a base64 data:image/png URI ready to drop into an <img> tag.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to capture full-page PNG screenshots for reports, previews, visual diffs, website archives, OCR input, or vision-model workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target URLs and rendered page contents are sent to an external Scavio service for screenshot processing.

Mitigation: Use only public or authorized pages, avoid confidential or regulated targets unless approved, and review Scavio handling terms before deployment.

Risk: The SCAVIO_API_KEY credential is required to call the screenshot API.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and keep it out of source code and logs.

Risk: Higher capture tiers consume more credits, with ultra costing 5 credits per successful capture.

Mitigation: Start with normal mode and escalate only when returned images are blank or incomplete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/website-screenshot-api)
- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=website-screenshot-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=website-screenshot-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON response examples and shell or Python request snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces instructions for returning a full-page PNG as an inline base64 data:image/png URI with URL, image_format, mode, image_bytes, response_time, credits_used, and credits_remaining metadata.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Render web pages and files into agent-ready markdown, structured data, screenshots, and PDFs via EnConvert, with a render_quality honesty score on every read.

This skill is ready for commercial/non-commercial use.

## Publisher:

[enconvert](https://clawhub.ai/user/enconvert)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to read URLs, search the web, discover site URLs, extract structured fields, and convert hosted files into markdown or PDF through EnConvert.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requested URLs and files to EnConvert's service for processing.

Mitigation: Use it only for content that fits the user's data-handling requirements, and avoid confidential files unless EnConvert processing is approved.

Risk: The skill requires a private EnConvert API key.

Mitigation: Store the key in ENCONVERT_API_KEY, do not print or hardcode it, and do not send it when fetching third-party source files or signed output URLs.

Risk: Rendered web content can be degraded by empty pages, blocked pages, bot walls, or JavaScript rendering issues.

Mitigation: Check and surface render_quality before relying on converted page content.

## Reference(s):

- [EnConvert Documentation](https://www.enconvert.com/docs)
- [ClawHub Skill Page](https://clawhub.ai/enconvert/skills/enconvert)
- [Publisher Profile](https://clawhub.ai/user/enconvert)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown, structured JSON, signed output URLs, screenshots, PDFs, and inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Perceive responses include a render_quality score; signed and presigned artifact URLs are time-limited and should be fetched without the API key.]

## Skill Version(s):

0.0.1 (source: frontmatter and changelog, released 2026-08-27)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Google Slides API integration with managed OAuth for creating presentations, adding slides, inserting content, and managing slide formatting through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect and modify Google Slides presentations through managed Maton OAuth connections. It supports presentation creation, slide/page lookup, thumbnails, batch updates, text, image, shape, and formatting operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Slides actions are routed through Maton and depend on the selected Google account and connection.

Mitigation: Confirm the intended Google account and connection before use, and specify a connection when multiple accounts are available.

Risk: Write or delete API calls can modify presentation content or remove objects.

Mitigation: Default to read and list calls, then require explicit user confirmation of the target resource, payload, and intended effect before POST, PUT, PATCH, or DELETE requests.

Risk: Long-lived API keys can be exposed through environment variables, logs, shell history, or command-line arguments.

Mitigation: Prefer Maton OAuth and the CLI credential store; when raw HTTP is unavoidable, never print or persist the key and feed authorization headers through stdin.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-slides)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Slides API Overview](https://developers.google.com/slides/api/reference/rest)
- [Google Slides Presentations](https://developers.google.com/slides/api/reference/rest/v1/presentations)
- [Google Slides Pages](https://developers.google.com/slides/api/reference/rest/v1/presentations.pages)
- [Google Slides BatchUpdate](https://developers.google.com/slides/api/reference/rest/v1/presentations/batchUpdate)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance, Configuration instructions]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Google Slides connection.]

## Skill Version(s):

1.1.0 (source: release evidence; skill frontmatter says 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

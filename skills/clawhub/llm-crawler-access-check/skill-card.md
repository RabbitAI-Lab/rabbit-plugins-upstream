## Description:

Checks a website's robots.txt to show whether AI search and training crawlers are allowed, blocked, or partially blocked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxaeo](https://clawhub.ai/user/maxaeo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and AI visibility teams use this skill to review a public robots.txt file and understand whether major AI answer engines can index, cite, or fetch the site.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested robots.txt edits can change whether a site appears in AI search, citation, or training workflows.

Mitigation: Review every proposed line before applying it and confirm the intended allow/block policy with the site owner.

Risk: A robots.txt result does not prove that crawlers can reach the site if CDN, WAF, bot-management, or IP reputation controls block access.

Mitigation: Treat the report as the first-gate check and verify server-side or CDN bot rules separately when crawler access still appears inconsistent.

Risk: Crawler names and operator policies can change after the bundled list was written.

Mitigation: Check the relevant operator's published crawler documentation before finalizing access guidance.

## Reference(s):

- [MaxAEO homepage](https://maxaeo.ai/)
- [ClawHub skill page](https://clawhub.ai/maxaeo/skills/llm-crawler-access-check)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown report with an allow/block table and optional robots.txt code block]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only check of one public robots.txt file; suggested robots.txt edits require user review before application.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

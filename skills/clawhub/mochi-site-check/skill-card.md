## Description:

Check one to five explicitly chosen public HTTPS URLs once for GET status, elapsed time, redirects, verified TLS and basic HTML SEO fields, saving local JSON and Markdown. Use for 网站巡检 or a basic page availability check; not vulnerability scanning, port probing, crawling or monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run a one-time check of up to five explicitly selected public websites, reviewing HTTP availability, redirects, TLS validation, response time, and basic static HTML SEO fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Website operators can see the requests and the host IP; saved reports contain the checked URLs and page metadata and may be shared with the configured model.

Mitigation: Use public URLs without credentials or session tokens, save reports in an approved workspace, and review them before sharing under the configured model provider’s data policy.

Risk: A one-time static check is not a complete SEO, security, or uptime assessment and may not reflect JavaScript-rendered pages.

Mitigation: Treat the report as a limited snapshot; verify important findings independently and use appropriate monitoring or security tools for those needs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/hznetnewpower/skills/mochi-site-check)
- [MochiLab](https://mochilab.bz)

## Skill Output:

**Output Type(s):** [JSON, Markdown]

**Output Format:** [Structured JSON and readable Markdown report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One-time checks of up to five selected public HTTPS URLs; no crawling, monitoring, vulnerability scanning, or JavaScript rendering.]

## Skill Version(s):

1.0.0 (source: README and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes images and video to produce natural-language scene descriptions and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media teams use this skill to summarize images or video clips, review scene analysis, and retrieve prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, or their URLs are sent to a remote service and may contain sensitive information.

Mitigation: Share only media authorized for remote processing; review data-handling requirements before use.

Risk: The skill silently creates or reuses a cloud identity and can retrieve reports linked to it.

Mitigation: Obtain user approval for cloud account linkage and report-history access before enabling the skill.

Risk: Authentication tokens persist in the local workspace data directory.

Mitigation: Protect access to that directory and remove or rotate stored tokens when access is no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-visual-summary-analysis)
- [Visual summary API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Natural-language scene description or structured report; report history as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and optionally save the result to a file.]

## Skill Version(s):

1.0.17 (source: ClawHub release; bundled frontmatter says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

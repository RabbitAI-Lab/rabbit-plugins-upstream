## Description:

Helps researchers investigate questions, verify citations against source registries, and produce evidence-graded reports and bibliographies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and other users can check reference lists for fabricated or incomplete citations and prepare research reports with graded evidence and auditable bibliographies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checking user-supplied reference URLs can trigger outbound requests beyond expected registries.

Mitigation: Avoid untrusted reference URLs and review network access before installing in shared environments.

Risk: External judging endpoints and proxy settings may receive citation claims or evidence.

Mitigation: Use only endpoints and proxies you control and are willing to share that material with.

Risk: A remotely reachable MCP server could accept requests from untrusted callers.

Mitigation: Keep the MCP server on stdio or loopback and do not expose it to untrusted callers.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Verification details](references/verification-details.md)
- [Medical research mode](references/medical-mode.md)
- [Report template](references/report-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Bibliography data]

**Output Format:** [Research reports and citation-verification results; optional BibTeX, RIS, CSV, JSON, and HTML exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [References receive verification verdicts and human-review flags; offline checks cannot confirm citations.]

## Skill Version(s):

3.11.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

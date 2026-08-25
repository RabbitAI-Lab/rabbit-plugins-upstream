## Description:

Triggers diagnostic analysis when users provide video URLs or files for reptiles such as lizards, snakes, and spiders, calls a server-side API for health checks, and returns a Pet Safety Guardian health report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit reptile or arachnid media for server-side health analysis and receive a structured health report with observations, risk notes, care suggestions, and report links. It also supports querying cloud-hosted historical health reports associated with the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload pet media or URLs to a remote service for analysis.

Mitigation: Review the remote-processing behavior before installation and avoid submitting sensitive local files or URLs.

Risk: The skill automatically creates or reuses an identity, queries cloud report history, and stores service tokens in the workspace data directory.

Mitigation: Install only where that account linkage and token persistence are acceptable, and clear workspace data when identity continuity is not desired.

Risk: Health analysis output is advisory and may be incorrect or incomplete for a specific animal.

Mitigation: Treat reports as health reference material and consult a qualified veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crawl-analysis)
- [API 接口文档](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown or JSON health analysis report, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include observations, potential disease warnings, care suggestions, historical report rows, and report links.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter states 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

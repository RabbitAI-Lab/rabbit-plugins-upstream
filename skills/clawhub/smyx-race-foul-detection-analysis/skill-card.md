## Description:

Analyzes pet racing videos to estimate start times, finish order, lane assignments, and possible false starts or lane crossings, returning structured results for referee review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Race referees and trainers can use the skill to review pet racing footage for start timing, finish order, lane assignments, and possible fouls. Its results are decision support; the on-site referee makes the final ruling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill may register accounts and retain credentials despite its advertised export-only mode.

Mitigation: Wait for fixes and explicit controls for account registration and saved credentials before using existing credentials.

Risk: The security evidence says footage may be uploaded, while remote retention and access controls are not established.

Mitigation: Avoid private footage until those controls are established, and restrict authenticated requests to trusted HTTPS destinations.

Risk: The security evidence does not establish analysis accuracy, so results may not be reliable enough to determine a race ruling on their own.

Mitigation: Treat the report as referee assistance and have the on-site referee review the evidence and make the final ruling.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-race-foul-detection-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis results, JSON, Markdown]

**Output Format:** [Structured JSON reports; Markdown tables for historical report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include start times, finish order, lane assignments, possible fouls, and report links.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata; artifact frontmatter differs: 1.0.21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

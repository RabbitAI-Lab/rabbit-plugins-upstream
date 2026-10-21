## Description:

Audits a public website for agent readiness by checking key-page discovery, AI crawler access, llms.txt, and MCP, then returns a score, category breakdown, and report link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mguarino4](https://clawhub.ai/user/mguarino4)

### License/Terms of Use:

MIT-0

## Use Case:

Website owners and developers use this skill to assess how agents discover important pages and access AI-relevant site content, or to compare a public domain in the Agent-Readiness Index.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted URLs may be sent to an external service and included in publicly viewable reports.

Mitigation: Submit only public URLs you are comfortable sharing with Gain Solutions; exclude private links and URLs containing secrets.

## Reference(s):

- [Agent-Readiness Audit](https://audit.gainsolutions.io/?utm_source=openclaw)
- [Audit methodology](https://audit.gainsolutions.io/methodology?utm_source=openclaw)
- [MCP discovery document](https://audit.gainsolutions.io/.well-known/mcp)
- [Agent-Readiness Index](https://audit.gainsolutions.io/index?utm_source=openclaw)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Structured scan or index results with a concise textual summary and report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scan results include a 0–100 score, verdict, category breakdown, and public report link; index tools return ranking or company-list data.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

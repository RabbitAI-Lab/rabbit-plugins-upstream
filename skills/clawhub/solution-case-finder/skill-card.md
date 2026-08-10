## Description:

Search PatSnap's TRIZ case library through its hosted MCP endpoint using plain HTTP, including keyword, technical-contradiction, SVOP, efficacy, Oxford-effect, patent-office, legal-status, applicant, and IPC/CPC criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwt1995](https://clawhub.ai/user/wwt1995)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to search PatSnap's TRIZ case library for analogous technical cases, cross-domain solution patterns, applied invention principles, and scientific effects relevant to an engineering problem.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided technical search criteria are sent to PatSnap/Eureka RD.

Mitigation: Avoid submitting trade secrets, NDA-protected details, personal data, proprietary technology, or export-controlled content; abstract or redact sensitive details before searching.

Risk: The HTTP helper depends on Bash, curl, jq, and a fixed hosted endpoint.

Mitigation: Review dependency availability and outbound network policy before installing or running the skill.

Risk: Analogous case results may be useful for inspiration but do not prove feasibility, freedom to operate, or legal safety.

Mitigation: Validate engineering fit independently and seek appropriate patent or legal review before relying on a case for product decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwt1995/skills/solution-case-finder)
- [Eureka RD TRIZ case finder](https://eureka.patsnap.com/rd/#/agentic?type=triz&start_from=clawhub&utm_source=clawhub&utm_medium=skill_listing&utm_campaign=triz_case_finder)
- [PatSnap TRIZ case MCP endpoint](https://ai-fabric.patsnap.com/mcp/patsnap-triz-case-library?APP_ID=Patsnap)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and structured case-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON results from the hosted MCP endpoint when using HTTP mode.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

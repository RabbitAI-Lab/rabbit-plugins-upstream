## Description:

Run AEO audits, preview branch audits, changed-page sitemap audits, local/private preview audits with explicit opt-in, sitemap origin rewriting, static-output audits, regression comparisons, site fixes, schema validation, and llms.txt generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site owners use the agent to audit websites and preview builds for answer-engine readiness, review and address site issues, validate structured data, generate llms.txt files, and compare reports for regressions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Proposed site changes could add misleading guidance or enable AI access or publication of project content.

Mitigation: Review proposed file changes and approve only the project paths and content needed.

Risk: Auditing private or local hosts can expose services that were not intended as targets.

Mitigation: Enable private-host auditing only for explicitly intended targets.

Risk: The skill invokes externally downloaded software, and the downloaded package was not reviewed.

Mitigation: Pin a reviewed exact package release when reproducibility matters.

## Reference(s):

- [Canonry AEO](https://canonry.ai)
- [ClawHub AEO skill release](https://clawhub.ai/arberx/skills/aeo)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Code, Files, Shell commands]

**Output Format:** [Audit and comparison reports, recommendations, and proposed project file changes in JSON or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Site changes and generated files require user approval; local or private targets require explicit opt-in.]

## Skill Version(s):

7.6.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

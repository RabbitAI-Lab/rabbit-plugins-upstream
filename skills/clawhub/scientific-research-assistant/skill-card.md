## Description:

Scientific Research Assistant supports literature review, data analysis and visualization, bioinformatics, drug discovery workflows, paper writing, and grant-planning assistance for research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, students, and technical research teams use this skill to plan and draft literature reviews, analyze scientific data, generate visualization or bioinformatics workflows, structure drug discovery investigations, and prepare papers or grant materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run local scientific commands and package installs in the user's project.

Mitigation: Use a virtual environment or sandbox and review generated commands before execution.

Risk: Research outputs may include incorrect analysis, unsuitable statistical methods, or misleading scientific conclusions.

Mitigation: Treat outputs as drafts and have qualified researchers validate methods, assumptions, citations, and conclusions before use.

Risk: Inputs or generated outputs may contain sensitive unpublished, regulated, or proprietary research data.

Mitigation: Avoid using sensitive data unless the workspace has appropriate access controls, and keep API keys in environment variables rather than files or logs.

Risk: External research APIs and databases may be unavailable, rate-limited, or return incomplete results.

Mitigation: Use local caches or retries where appropriate and verify important findings against authoritative sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/scientific-research-assistant)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, Python code or snippets, shell commands, configuration guidance, and research workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write project output files for reports, analyses, plots, and generated scripts.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

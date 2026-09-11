## Description:

时空智能分析法 guides agents through sourced spatiotemporal research by combining longitudinal timelines, cross-sectional comparison, convergence judgment, confidence labeling, report templates, and optional Chinese PDF output conventions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kingsunzhang2026-oss](https://clawhub.ai/user/kingsunzhang2026-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and agent developers use this skill to produce source-grounded research reports that combine timelines, comparative positioning, and explicit confidence judgments. It is intended for deeper research and competitive analysis tasks rather than one-line factual lookups, real-time news monitoring, or code audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags broad skill-management instructions that may affect workflows beyond a single research task.

Mitigation: Narrow the skill triggers and isolate or remove lifecycle-management guidance before deploying it in a shared agent environment.

Risk: The security evidence flags persistent home-directory writes and file-reading behavior.

Mitigation: Review cache and output paths before use, require user-confirmed destinations, and avoid running the skill in sensitive workspaces.

Risk: The security evidence flags an unsafe external Python import.

Mitigation: Replace hard-coded local imports with reviewed, pinned dependencies before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kingsunzhang2026-oss/skills/spatiotemporal-analysis)
- [Methodology](references/methodology.md)
- [Data sources](references/data_sources.md)
- [Output conventions and source quirks](references/output-conventions-and-source-quirks.md)
- [Chinese PDF output recipe](references/markdown-to-pdf-zh.md)
- [Writing baseline](references/writing_baseline.md)
- [Convergence probability table](templates/convergence_table.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown research reports with sourced claims, confidence labels, tables, JSON report templates, Python CLI guidance, and optional PDF build commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs emphasize source URLs, timestamps, explicit data gaps, citation coverage checks, and restrained Chinese PDF formatting when PDF delivery is requested.]

## Skill Version(s):

2.0.2 (source: ClawHub release metadata; artifact frontmatter says 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

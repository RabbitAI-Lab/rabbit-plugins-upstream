## Description:

Generates a Chinese HTML patent monitoring report for base-station antenna activity across 17 named companies, classifying results into vibrator, radome, reflector, and other technical branches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, IP teams, and telecom antenna engineers use this skill to monitor recent base-station antenna patent activity from selected competitors and produce a structured Chinese HTML report with classifications, keyword summaries, and patent tables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External or crafted patent fields could alter the generated HTML report because the security evidence notes that patent fields are rendered without escaping.

Mitigation: Use only trusted patent JSON or trusted MCP-sourced data, and review or sanitize generated reports before sharing them.

Risk: The report may be written to an unexpected location when output-directory configuration is used.

Mitigation: Verify the intended output path before running the skill, especially when EUREKA_PYTHON_OUTPUT_DIR or custom output arguments are set.

Risk: Readers may over-trust the report as live MCP data when the data source is unclear.

Mitigation: Label the source of the patent data and avoid treating the report as verified live MCP output unless the MCP configuration and source are confirmed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/base-station-antenna-monitor)
- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, HTML files]

**Output Format:** [Python script execution guidance and generated HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports configurable monitoring window, optional patent JSON input, retrieval cap, and output path.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

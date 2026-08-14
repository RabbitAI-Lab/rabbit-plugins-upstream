## Description:

CSV文件处理专家 helps agents inspect, clean, merge, split, convert, and export CSV data, including schedule and cost CSV workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and automation teams use this skill to guide CSV profiling, cleaning, merging, splitting, type conversion, and export tasks for engineering, construction, finance, schedule, and cost data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill requests broad execution or network-style authority that is not clearly scoped to CSV work.

Mitigation: Review each proposed operation before execution, keep use limited to local CSV files, and require confirmation before running shell commands or sending callback or API requests.

Risk: CSV transformations can overwrite or alter local data if paths are ambiguous.

Mitigation: Use explicit input and output paths, write transformed files to a separate directory, and keep backups of important source CSV files.

Risk: Malformed CSV rows may be skipped or parsed incorrectly during cleanup.

Mitigation: Inspect row counts, parser warnings, and sample output before relying on cleaned, merged, or converted data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/csv-handler)
- [SkillHub skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with code blocks, shell snippets, and JSON-style result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose CSV output files and explicit output paths when the agent is asked to transform local CSV data.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

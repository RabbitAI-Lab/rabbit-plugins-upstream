## Description:

Use when 学生或家长询问“这个分数能上哪个学校”、分数或位次对应院校、怎么冲稳保、有哪些升学路径、强基怎么走、综评怎么走，或需要中国高考选校、选专业、志愿填报、专项计划、公费师范、军警、港澳及中外合作规划。

This skill is ready for commercial/non-commercial use.

## Publisher:

[sarry12227](https://clawhub.ai/user/sarry12227)

### License/Terms of Use:

MIT-0

## Use Case:

Students, parents, and education-planning agents use this skill to plan China Gaokao school, major, and pathway choices from an anonymous confirmed profile and validated public-source evidence. It produces traceable rank ranges, school tiers, pathway recommendations, and next actions while preserving uncertainty and source coverage.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Admissions recommendations can be misleading when current-year public sources are unavailable, stale, conflicting, or incomplete.

Mitigation: Keep evidence status and coverage visible, stop precise adoption on conflicts, and independently verify important recommendations against official current-year admissions publications before acting.

Risk: The workflow can process sensitive student planning details and writes a recoverable local journal and anonymous report.

Mitigation: Avoid collecting names, phone numbers, addresses, credentials, communication IDs, and other identifiers; keep the workspace private and redact any report before sharing.

Risk: The skill runs local Python commands and downloads public admissions materials.

Mitigation: Install only from a trusted, reviewed source, prefer HTTPS sources, and preserve secure download limits and source validation before using downloaded content.

Risk: Public education data may not carry redistribution rights even when the code license is permissive.

Mitigation: Publish only materials with explicit redistribution permission; otherwise retain source URLs, minimal structured facts, and content hashes for traceability.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sarry12227/skills/pathway-atlas)
- [README](README.md)
- [Data sources and redistribution policy](DATA_SOURCES.md)
- [Source policy](references/source-policy.md)
- [Host workflow guide](references/host-workflow.md)
- [Security policy](SECURITY.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with optional DOCX export and evidence-status annotations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Anonymous by default; recommendations depend on the confirmed profile, available host capabilities, and validated public-source evidence.]

## Skill Version(s):

0.1.1 (source: server release evidence, pyproject.toml, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

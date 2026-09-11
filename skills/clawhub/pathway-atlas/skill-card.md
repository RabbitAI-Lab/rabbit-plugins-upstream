## Description:

Use when 学生、家长或老师询问“这个分数能上哪个学校”、怎样看位次和冲稳保、有哪些升学路径、强基怎么走、综评怎么走，或需要中国高考选校、选专业、志愿填报及专项、公费师范、军警、港澳和中外合作规划；结合成绩、选科、兴趣和家庭条件，弄清值得准备的选择与下一步行动。

This skill is ready for commercial/non-commercial use.

## Publisher:

[sarry12227](https://clawhub.ai/user/sarry12227)

### License/Terms of Use:

MIT

## Use Case:

Students, families, teachers, and their supporting agents use this skill to collect an anonymous planning profile, verify public Chinese college-admission sources, compare schools, majors, and pathway options, and produce clear next steps. It is intended for evidence-based planning support, not guaranteed admission decisions or official application submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Planning state, retrieved evidence, and generated reports may contain sensitive student context if the user provides it.

Mitigation: Keep workspaces private and avoid collecting names, phone numbers, credentials, exact addresses, communication IDs, or unnecessary personal identifiers.

Risk: Unpinned installer commands can fetch changing third-party content.

Mitigation: Prefer a reviewed repository checkout or pinned installer before installing or updating the skill.

Risk: College-planning outputs can include estimates, incomplete source coverage, or public-source uncertainty.

Mitigation: Disclose assumptions and source limits, prefer verified public sources, and treat outputs as planning support rather than admission guarantees.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sarry12227/skills/pathway-atlas)
- [README](README.md)
- [Quick planning workflow](references/quick-planning.md)
- [Host workflow guide](references/host-workflow.md)
- [Source policy](references/source-policy.md)
- [Research recovery guide](references/research-recovery.md)
- [Conversation output template](references/conversation-output.md)
- [Exam cutoff calibration](references/exam-cutoff-calibration.md)
- [School report estimation](references/school-report-estimation.md)
- [National opportunity order](references/national-opportunity-order.md)
- [Pathway comparison](references/pathway-comparison.md)
- [Data sources and boundaries](DATA_SOURCES.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Conversational text and Markdown reports, with optional local files and shell commands handled by the agent host]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce anonymous planning notes, evidence summaries, Markdown reports, and optional DOCX exports when host capabilities allow.]

## Skill Version(s):

0.2.4 (source: server release metadata, pyproject.toml, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

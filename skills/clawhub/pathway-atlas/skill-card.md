## Description:

Use when 学生、家长或老师询问“这个分数能上哪个学校”、怎样看位次和冲稳保、有哪些升学路径、强基怎么走、综评怎么走，或需要中国高考选校、选专业、志愿填报及专项、公费师范、军警、港澳和中外合作规划；结合成绩、选科、兴趣和家庭条件，弄清值得准备的选择与下一步行动。

This skill is ready for commercial/non-commercial use.

## Publisher:

[sarry12227](https://clawhub.ai/user/sarry12227)

### License/Terms of Use:

MIT

## Use Case:

Students, families, teachers, and advising agents use this skill to collect an anonymous planning profile, verify public Chinese admissions information, compare schools, majors, and pathway options, and produce clear next actions. It supports step-by-step consultation before delivering personalized planning guidance after the profile is confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may store anonymous planning profiles, public-source evidence, and generated reports in the agent's private workspace.

Mitigation: Do not provide names, phone numbers, ID numbers, credentials, private local paths, or nonpublic student records; keep reports anonymous.

Risk: OCR, QR, attachment, or external source handling can involve data outside the local planning conversation.

Mitigation: Use public or redacted materials, and require explicit approval before any external OCR or QR service is used.

Risk: Admissions recommendations can be affected by incomplete public sources, time-sensitive policies, or estimation uncertainty.

Mitigation: Present source coverage and uncertainty in the planning output, and treat final applications, registrations, and decisions as actions to verify through official channels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sarry12227/skills/pathway-atlas)
- [PathwayAtlas README](https://github.com/sarry12227/pathway-atlas#readme)
- [Using PathwayAtlas](docs/using-pathway-atlas.md)
- [Host workflow guide](references/host-workflow.md)
- [Questionnaire](references/questionnaire.md)
- [Quick planning](references/quick-planning.md)
- [Source policy](references/source-policy.md)
- [Retrieval playbook](references/retrieval-playbook.md)
- [Research recovery](references/research-recovery.md)
- [Province catalog](references/provinces/index.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Conversational text and Markdown, with optional generated Markdown or DOCX reports and JSON-backed planning artifacts handled by the agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should disclose source coverage, estimation limits, and uncertainty where they affect admissions planning; generated planning records are intended for the agent's private workspace.]

## Skill Version(s):

0.2.8 (source: pyproject.toml, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

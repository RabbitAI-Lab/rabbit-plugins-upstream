## Description:

多元星途 · PathwayAtlas helps students, families, and teachers plan China gaokao school, major, and pathway choices through step-by-step intake, public-source verification, evidence-aware analysis, and clear next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sarry12227](https://clawhub.ai/user/sarry12227)

### License/Terms of Use:

MIT

## Use Case:

Students, families, teachers, and education-planning agents use this skill to compare schools, majors, ordinary admission choices, and alternative gaokao pathways such as Strong Foundation, comprehensive evaluation, targeted programs, public-funded teacher education, military or police routes, Hong Kong/Macau options, and international cooperation programs. It is intended to turn an anonymous confirmed profile and verified public admissions evidence into readable planning guidance, priority actions, and evidence gaps.

### Deployment Geography for Use:

Global; content scope is China gaokao and related admissions planning.

## Known Risks and Mitigations:

Risk: The skill runs local Python workflow files and retrieves public admissions materials.

Mitigation: Install only from the intended repository source, review the skill before execution, and keep the planning workspace private.

Risk: A student or family could disclose personal identifiers or secrets during planning.

Mitigation: Use an anonymous profile and do not provide student names, phone numbers, IDs, credentials, cookies, or local file paths.

Risk: Public admissions sources, PDFs, QR links, or HTTP-only pages may be incomplete, stale, or hard to authenticate.

Mitigation: Use authenticated and corroborated sources where available, preserve evidence gaps, and treat generated advice as planning support rather than an admission guarantee.

## Reference(s):

- [README](README.md)
- [Host workflow guide](references/host-workflow.md)
- [Questionnaire](references/questionnaire.md)
- [Retrieval playbook](references/retrieval-playbook.md)
- [Research recovery guide](references/research-recovery.md)
- [Source policy](references/source-policy.md)
- [Data sources and redistribution policy](DATA_SOURCES.md)
- [ClawHub skill page](https://clawhub.ai/sarry12227/skills/pathway-atlas)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Conversational Chinese guidance with Markdown report output and optional DOCX export when supported.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes evidence status, source coverage, uncertainty, prioritized actions, and explicit gaps when materials are unavailable or insufficient.]

## Skill Version(s):

0.1.7 (source: pyproject.toml, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Audits installed AI skills by inventorying and classifying them, detecting overlap and conflicts, scoring maturity, and recommending which to keep, merge, improve, or remove.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songzhou666](https://clawhub.ai/user/songzhou666)

### License/Terms of Use:

MIT

## Use Case:

Developers use SkillMedic to review installed AI skills, find duplicate capabilities and trigger conflicts, assess maturity, and decide which skills to retain, combine, improve, or remove.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this skill suspicious, citing access scope and persistent changes, along with a possible script substitution weakness; the review is incomplete.

Mitigation: Review the reported access scope and rubric-update behavior before installing. Treat the assessment as partial: 32 of 36 components were fully inspected, and static analysis of tool-misuse patterns was degraded.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/songzhou666/skills/skill-medic)
- [Source repository (server-resolved provenance)](https://github.com/songzhou666/skill-medic)
- [Server-resolved source commit](https://github.com/songzhou666/skill-medic/commit/dbc5834d131cdbe481867681292a0b31fa713ba6)
- [CLI guide](references/cli-guide.md)
- [Scoring rubric details](references/rubric-detail.md)
- [Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Skill inventory and audit reports with conflict findings, maturity scores, and recommendations; structured JSON is also used for intermediate data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report detail varies by inventory size; CLI commands can save generated artifacts under the selected project’s .medic directory.]

## Skill Version(s):

0.1.3 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

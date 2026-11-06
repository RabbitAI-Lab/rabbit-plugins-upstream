## Description:

Audits a completed coding task by extracting session evidence and comparing it with a numbered specification list, then produces a coverage matrix and concrete counterexamples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to review a completed development task against its requirements, identify missing evidence or likely gaps, and prepare concrete follow-up checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session evidence or generated reports may contain private paths or tool descriptions.

Mitigation: Select only the session and repository relevant to the task, and keep reports within the intended audience.

Risk: Command counts and partial session evidence can be mistaken for proof that requirements were satisfied or tests passed.

Mitigation: Review command results and repository changes directly, and base coverage conclusions on the available evidence.

## Reference(s):

- [Project homepage](https://github.com/z-Zihan/awesome-skills)
- [ClawHub release page](https://clawhub.ai/z-zihan/skills/delivery-spec-audit)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown audit report with a numbered specification list, coverage matrix, verification summary, and action checklist.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are based on the supplied task specifications and session or repository evidence; command counts do not establish pass or fail.]

## Skill Version(s):

1.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

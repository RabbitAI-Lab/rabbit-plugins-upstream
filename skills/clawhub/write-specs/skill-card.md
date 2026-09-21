## Description:

Use when the user needs to create or refine a feature SPEC SDD before implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to clarify feature, bugfix, refactor, API, infrastructure, frontend, or documentation work before implementation. It gathers project facts, asks requirement questions in Portuguese, writes a SPEC SDD under `.specs/`, and waits for approval before handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads project files and turns them into planning guidance, so missing or misunderstood context could produce an inaccurate SPEC.

Mitigation: Review the generated SPEC and require explicit user approval before implementation begins.

Risk: The workflow writes a SPEC file under `.specs/` and may ask to create a GitHub Issue after approval.

Mitigation: Inspect the file path and generated Markdown before approving, and only create the Issue after the user explicitly accepts the handoff.

Risk: The workflow conducts user-facing approvals and requirements discussions in Portuguese.

Mitigation: Use it only when a Portuguese-language requirements workflow is acceptable for the team.

## Reference(s):

- [SPEC SDD template](references/spec-sdd-template.md)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/write-specs)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Metadata source URL](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown SPEC document plus Portuguese question rounds and approval prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes the SPEC to `.specs/SPEC-{YYYYMMDD}-{feature}.md`; may ask whether to create a GitHub Issue after approval.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

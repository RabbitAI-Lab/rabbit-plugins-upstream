## Description:

Maps candidate skills to an interview plan and builds an interview agenda.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters and interview teams use this skill to compare a candidate's skills with role requirements and prepare a focused interview agenda.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Candidate profile data is processed locally and may appear in a generated agenda.

Mitigation: Use only candidate information authorized for interview planning, and review the agenda before sharing.

Risk: Agenda generation writes a Markdown file under the chosen output directory.

Mitigation: Choose a writable directory appropriate for candidate data and review its contents after generation.

## Reference(s):

- [Interview Planning Studio on ClawHub](https://clawhub.ai/wxt-ai/skills/interview-planning-studio)
- [Candidate Skills Mapper documentation](artifact/operations/upstream/README.md)
- [Interview Agenda Builder documentation](artifact/operations/downstream/README.md)

## Skill Output:

**Output Type(s):** [JSON, Markdown]

**Output Format:** [JSON interview plan or agenda result; local Markdown agenda file when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agenda generation requires a writable output directory supplied by the user.]

## Skill Version(s):

3.0.0 (source: skill frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

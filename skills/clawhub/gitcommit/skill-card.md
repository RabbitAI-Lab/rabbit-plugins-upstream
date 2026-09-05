## Description:

Helps an agent prepare, review, and, after explicit confirmation, create Conventional Commit plans from uncommitted repository changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlykan](https://clawhub.ai/user/wlykan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to turn current repository changes into reviewable, atomic Conventional Commit plans and commit messages before any Git write operation is performed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill inspects uncommitted repository changes while preparing commit plans.

Mitigation: Review the displayed plan and avoid including sensitive paths or secret material in a commit unless intentionally approved.

Risk: A commit operation can alter repository history by adding a new commit after confirmation.

Mitigation: The skill requires an explicit confirmation after presenting the complete plan before staging or committing changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wlykan/skills/gitcommit)
- [Publisher profile](https://clawhub.ai/user/wlykan)

## Skill Output:

**Output Type(s):** [analysis, markdown, shell commands, guidance]

**Output Format:** [Markdown commit plan with Conventional Commit messages and Git command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation before staging or committing changes.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

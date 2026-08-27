## Description:

Provides review-workflow scaffolding for context, evidence, and output so detailed reviews can produce consistent, comparable findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and reviewers use this skill at the start of detailed reviews to establish context, inventory scope, capture evidence, structure findings, and document contingencies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill encourages repository inspection and evidence capture, which can expose local project details if used in an unintended workspace.

Mitigation: Use it only in workspaces where local file review is intended and keep captured evidence scoped to the review.

Risk: Review findings can be incomplete if the shared scaffolding is used without the relevant domain-specific checklist.

Mitigation: Pair this skill with the appropriate domain review workflow before concluding the assessment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-review-core)
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with checklist items and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces review scaffolding and evidence-capture structure; it does not execute code by itself.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

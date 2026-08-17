## Description:

Produces a durable onboarding document for a codebase with cited sections for system overview, dependency use, startup flow, auth flow, and important files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to generate or refresh a repository onboarding guide after joining, revisiting, or handing off a project. It focuses the agent on evidence-backed explanations with file:line citations rather than generic framework summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill inspects repository files and may surface sensitive implementation details in the generated onboarding document.

Mitigation: Run it only in repositories where this inspection is intended, and review the generated ONBOARDING.md before committing or sharing it.

Risk: The skill creates or updates an onboarding file in the workspace.

Mitigation: Check whether ONBOARDING.md or docs/ONBOARDING.md will be modified, and review the diff before accepting the change.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown document plus concise chat summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes ONBOARDING.md at the repository root, or docs/ONBOARDING.md when a docs directory exists.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

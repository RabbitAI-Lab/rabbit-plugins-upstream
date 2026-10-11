## Description:

Guides agents through parallel reviews, delegated implementation, and pipeline workflows with clear ownership and verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to coordinate multiple agents on independent reviews and implementation tasks, with bounded assignments, integration checks, and honest completion reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Parallel workers may make overlapping edits or report incomplete work as finished.

Mitigation: Assign exclusive file ownership, inspect returned changes, and run post-integration checks before reporting completion.

Risk: Background workers or shared task-status files may require additional oversight during sensitive work.

Mitigation: Review worker scopes and task status, then verify worker shutdown before closing the work.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms)
- [Dispatch contract](references/dispatch-contract.md)
- [Worker lifecycle](references/worker-lifecycle.md)
- [Review and delivery](references/review-and-delivery.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with task briefs, review findings, and verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include worker assignments, status reports, and suggested checks.]

## Skill Version(s):

5.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

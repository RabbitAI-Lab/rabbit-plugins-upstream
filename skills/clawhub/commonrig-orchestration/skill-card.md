## Description:

Guides coding agents in delegating bounded work to subagents, assigning disjoint file ownership, and verifying results before integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[commonrig](https://clawhub.ai/user/commonrig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to scope subagent coding assignments, coordinate parallel work, and review changes before reporting completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delegated coding work may change unintended project files or introduce incorrect changes.

Mitigation: Assign exact files and acceptance checks, inspect returned changes, and verify behavior before integration.

Risk: Delegation may lead to unauthorized spending, publishing, credential use, or git operations.

Mitigation: Keep normal approval boundaries for external actions and credentials; reserve git writes for the authorized orchestrator.

## Reference(s):

- [CommonRig homepage](https://commonrig.com)
- [CommonRig free orchestration protocol](https://commonrig.com/v1/sample)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Text or Markdown briefs and review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes file ownership, acceptance checks, and verification steps.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

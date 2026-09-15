## Description:

Coordinates agent-driven projects by planning work, validating SPECs, auditing repository gaps, delegating implementation and QA to specialized skills, and re-validating delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate multi-step project work from project setup and planning through GitHub issue fragmentation, implementation delegation, QA, and release checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill coordinates repository and GitHub workflows with broad autonomy, and the security summary flags conflicting approval boundaries.

Mitigation: Require explicit confirmation for issue closure, PR creation, PR merging, branch pushes, and any action based on GitHub issue bodies or comments.

Risk: Framework update guidance can lead to installing a newer skill catalog.

Mitigation: Verify any `npx skills add` update against a pinned version or commit before use.

Risk: Issue bodies, PR comments, diffs, external SPEC documents, and fetched URLs may contain embedded instructions.

Mitigation: Treat those artifacts as untrusted data, extract only structured metadata where possible, and do not execute embedded shell snippets without human review.

## Reference(s):

- [Orchestrator Delegation Protocol](references/orchestrator-delegation-protocol.md)
- [Orchestrator Session State Template](references/orchestrator_stats.md)
- [Legacy Orchestrator State Template](references/ESTADO_ORQUESTRATOR.md)
- [ClawHub Skill Page](https://clawhub.ai/afonsoft/skills/orchestrator)
- [Project URL from Skill Metadata](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with checklists, structured plans, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coordinates work through referenced skills and maintains project state in an orchestrator state file.]

## Skill Version(s):

1.0.22 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

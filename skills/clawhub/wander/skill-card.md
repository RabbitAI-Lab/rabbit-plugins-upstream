## Description:

Close the loop on long-running remote work by choosing a platform-appropriate completion signal, monitoring in the background, notifying on finish, and verifying the outcome, including with Wander scripts for GitHub Actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erergb](https://clawhub.ai/user/erergb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to monitor long-running CI, mobile builds, deployments, and releases through the system that owns each task's status, then inspect the terminal result and failure details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the skill suspicious because reported GitHub Actions reruns and remote repository pushes may exceed its described monitoring purpose; the scan evidence is incomplete.

Mitigation: Review the reported rerun and push behavior and resolve the missing referenced paths before installing. Install only if you understand and accept that use may trigger remote jobs or publish repository changes.

## Reference(s):

- [Wander repository](https://github.com/ERerGB/wander)
- [Wander v1 scope: GitHub Actions today](https://github.com/ERerGB/wander/blob/main/README.md#v1-scope-github-actions-today)
- [Wander edge cases](https://github.com/ERerGB/wander/blob/main/EDGE_CASES.md)
- [Wander coffee break guide](https://github.com/ERerGB/wander/blob/main/COFFEE_BREAK.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Platform-aware monitoring steps and examples for checking terminal status and retrieving failure details.]

## Skill Version(s):

1.0.8 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Forge provides a forge-agnostic driver contract and helper interface for GitHub, GitLab, and Gitea PR, issue, merge, auth, visibility, reference-format, dependency, and review-bot workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent-workflow maintainers use this skill to design or operate forge-portable PR, MR, issue, merge, auth, visibility, dependency, and review-bot flows without hardcoding a single git host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When the bundled shell helper is sourced, its functions can use existing gh, glab, or tea authentication to create, edit, or merge PRs and issues.

Mitigation: Tie helper calls to explicit user intent, prefer DRY_RUN=1 when checking command shape, and review merge or edit actions before execution.

Risk: Some GitLab and Gitea behavior is documented as adapter boundary or follow-up work, so unsupported operations may degrade or return boundary messages.

Mitigation: Check the capability matrix and query the driver capability before relying on native dependency links, sub-issues, bot review, or Gitea API-backed methods.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/forge)
- [Driver interface](artifact/driver-interface.md)
- [Capability matrix](artifact/capability-matrix.md)
- [Dispatch guide](artifact/dispatch.md)
- [Adapter boundary guide](artifact/adapters.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell command contracts and optional bash helper functions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes normalized forge method contracts, capability flags, dispatch rules, and degradation guidance.]

## Skill Version(s):

0.1.3 (source: server release metadata and changelog, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

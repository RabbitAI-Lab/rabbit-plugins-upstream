## Description:

Forge defines a forge-agnostic git-host driver contract for GitHub, GitLab, and Gitea workflows through normalized driver methods, capability flags, and --forge dispatch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and workflow engineers use this skill to design, reason about, and implement forge-portable PR, MR, issue, merge, authentication, visibility, and dependency operations across GitHub, GitLab, and Gitea. It helps agents choose adapter behavior, dispatch rules, and graceful degradation paths when a forge lacks a native capability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included shell helper can perform PR, MR, issue, and merge operations when explicitly sourced and called.

Mitigation: Use the helper only in repositories where those forge operations are intended, review generated command shapes, and rely on dry-run or tests before live use.

Risk: Some GitLab and Gitea adapter behavior is documented as a boundary or Phase 2 follow-up rather than fully implemented behavior.

Mitigation: Check the capability matrix and adapter documentation before relying on a native operation, and use documented degradation paths when support is absent.

## Reference(s):

- [Forge Skill Page](https://clawhub.ai/drumrobot/skills/forge)
- [Driver Interface](artifact/driver-interface.md)
- [Capability Matrix](artifact/capability-matrix.md)
- [Dispatch](artifact/dispatch.md)
- [Adapters](artifact/adapters.md)
- [Forge Driver Helper](artifact/resources/forge-driver.sh)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Bash helper functions and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include forge CLI command shapes and adapter boundary guidance; shell helper behavior depends on the resolved forge and caller environment.]

## Skill Version(s):

0.1.2 (source: server release metadata and CHANGELOG, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

ReqPlan-v3 is a project lifecycle management skill that guides software engineering work through analysis, design, implementation, verification, and final judgment phases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songzhou666](https://clawhub.ai/user/songzhou666)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to manage complex software tasks that need staged requirements analysis, design, implementation, verification, and quality audit artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can auto-activate on broad software-development phrases and create persistent project files before clear user consent.

Mitigation: Prefer explicit invocation with /reqplan and review planned writes before allowing creation of .agent/harness or docs/harness files.

Risk: Normal operation may include source-code changes and verification commands that install dependencies.

Mitigation: Use it in version-controlled repositories, inspect changes before commit, and run it only where dependency installation and code edits are acceptable.

Risk: Generated project artifacts may contain sensitive project context if used in repositories with secrets or customer data.

Mitigation: Avoid use on sensitive workspaces unless artifact writes are reviewed first, and keep harness artifacts out of public commits when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songzhou666/skills/reqplan-v3)
- [Server-resolved source repository](https://github.com/songzhou666/ReqPlan-v3)
- [README](README.md)
- [Baton protocol](protocols/baton-protocol.md)
- [Artifact templates](artifacts/template-artifacts.md)
- [Quality system](quality-control/00-quality-system.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, source-code edits, shell command recommendations, and project harness files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update .agent/harness and docs/harness artifacts during normal use.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 5.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

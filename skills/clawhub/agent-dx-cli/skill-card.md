## Description:

Guides the design, review, and refactoring of agent-facing CLIs for predictable behavior, layered safeguards, and efficient context use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to evaluate agent-facing CLI contracts, implement authorized improvements, and report scored behavioral evidence and remaining limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business-effect tests may change live resources.

Mitigation: Run them only with authorization in isolated fixtures and confirm targets before execution.

Risk: Credentials may leak through CLI arguments, errors, or logs.

Mitigation: Scope real credentials narrowly, keep them out of logs, and check output for exposed secrets.

## Reference(s):

- [Agent DX CLI release](https://clawhub.ai/agenticweb4/skills/agent-dx-cli)
- [GWS practice](references/gws.md)
- [SKILL+CLI authoring](references/skill-cli.md)
- [Pinned Google Workspace CLI example](https://github.com/googleworkspace/cli/tree/a3768d0e82ad83cca2da97724e46bea4ff0e6)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Code, Shell commands]

**Output Format:** [Markdown with scores, evidence, and proposed or authorized CLI changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scores are tied to the tested artifact and version; acceptance requires verified behavior.]

## Skill Version(s):

0.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

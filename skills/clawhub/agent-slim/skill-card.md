## Description:

Agent 瘦身：盘点、注入测量、发布闸门、回滚；不删原件。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT

## Use Case:

开发者和 Agent 运维人员可用它盘点常驻上下文与存储内容、测量注入预算，并生成可审阅、可回滚的减负计划和发布前检查结果。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review calls out restore-path and verification weaknesses.

Mitigation: Review the proposed paths and transaction manifest hashes before applying changes; verify the result and recovery plan before restoring.

Risk: The security review identifies a bearer-token redirect risk for MCP probing.

Mitigation: Probe only trusted MCP endpoints and avoid sending bearer tokens where redirect behavior has not been reviewed.

Risk: The security review flags an extra icon-generation capability and broad tool scope.

Mitigation: Review whether icon generation is needed for the task and restrict access to the files and commands required for the selected audit or release check.

## Reference(s):

- [Usage and command behavior](docs/usage.md)
- [Safety boundaries and allowlist](docs/safety.md)
- [Injection measurement and release gate](docs/injection-measurement.md)
- [Context model](references/context-model.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Shell commands, Code, Guidance]

**Output Format:** [JSON audits and plans, Markdown reports, and generated restore scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the audited scope; estimates are labeled, and cold-storage moves are not counted as token savings.]

## Skill Version(s):

0.2.0 (source: release evidence, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

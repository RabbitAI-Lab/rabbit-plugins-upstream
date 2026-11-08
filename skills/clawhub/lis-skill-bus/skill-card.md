## Description:

本地 Skill 联动总线（MCP 安装器）：连接 cad-file-reader 与算量 Skill，复用 cad-contract/v1，避免重复解图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT

## Use Case:

供使用 CAD 识图与工程量算量技能的工程师安装和使用，通过本地 MCP 或 CLI 共享项目状态及 cad-contract/v1 识图契约，避免对同一张图重复解析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contract lookup may reuse a contract after a source fingerprint mismatch, which could silently pass stale drawing data to downstream skills.

Mitigation: Before using a returned contract, compare its source fingerprint and file provenance with the current drawing; reject mismatches and rerun cad-file-reader.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lisong2003-lgtm/skills/lis-skill-bus)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions]

**Output Format:** [MCP tool responses and JSON project state/contracts; CLI command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local project state and CAD contract data; no network access is required.]

## Skill Version(s):

0.1.10 (source: frontmatter, changelog, released 2026-11-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

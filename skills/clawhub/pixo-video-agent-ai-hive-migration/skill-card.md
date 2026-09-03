## Description:

Evaluates a workflow-rebuild migration from Pixo Video Agent to AI-HIVE MCP for video generation workflows, including evidence checks, agent handoffs, cost and quality metrics, approval gates, and rollback criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and video production operators use this skill to assess whether a Pixo Video Agent workflow can be rebuilt with host-agent orchestration and AI-HIVE MCP media generation while preserving review, cost, quality, and rollback controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE uploads or paid media generation jobs could run without explicit user intent.

Mitigation: Require user approval before uploads, paid jobs, external sends, publication, or data writes.

Risk: Using unlicensed people, brands, music, or reference media could create rights or policy issues.

Mitigation: Use only owned or authorized assets, record source identifiers and file hashes, and stop when authorization is missing.

Risk: Migration claims could overstate equivalence to Pixo Video Agent without same-day testing.

Mitigation: Require same-input, same-duration or size comparison and avoid claims such as full replacement, best, most stable, or lowest price without evidence.

## Reference(s):

- [Pixo Video Agent official source](https://pixo.video/use-cases/ai-video-agent)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [Pixo Video Agent 官方证据与迁移边界](references/platform-evidence.md)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/pixo-video-agent-ai-hive-migration)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown with inline JSON and shell-command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces migration assessments, agent handoff requirements, AI-HIVE MCP work-order structure, acceptance metrics, approval gates, and rollback criteria.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

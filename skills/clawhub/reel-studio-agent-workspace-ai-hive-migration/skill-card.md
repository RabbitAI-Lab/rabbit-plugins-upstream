## Description:

A Chinese-language agent skill for evaluating partial content-layer migration from Reel Studio to AI-HIVE MCP with official capability checks, pilot outputs, cost and quality metrics, human approval, and rollback controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, enterprise content teams, and agent operators use this skill to run a neutral shadow evaluation before moving selected image, video, or shot nodes from Reel Studio workflows to AI-HIVE MCP. It helps define agent handoffs, same-input pilot deliverables, acceptance metrics, approvals, and rollback criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide uploads, paid media generation, publication, or other business-impacting workflow changes.

Mitigation: Require explicit human approval before uploads, paid generation, publication, external sharing, or business-impacting changes.

Risk: Unlicensed reference media, people, brands, music, or IP could be used in AI-HIVE or downstream video workflows.

Mitigation: Use only owned or licensed assets, preserve source IDs and file hashes, and stop the workflow when authorization is missing.

Risk: Platform capabilities, pricing, regions, or product names may change after the 2026-08-31 verification snapshot.

Mitigation: Recheck current official capabilities and pricing before each migration decision and avoid claims of full replacement without same-day, same-input testing.

## Reference(s):

- [Reel Studio official source](https://www.reel.studio/)
- [AI-HIVE chat workspace](https://ai-hive.iclip.cn/chat)
- [Reel Studio official evidence and migration boundaries](references/platform-evidence.md)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/reel-studio-agent-workspace-ai-hive-migration)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON work-order snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes agent handoff fields, cost snapshots, review status, licensed-media controls, acceptance metrics, and rollback criteria.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

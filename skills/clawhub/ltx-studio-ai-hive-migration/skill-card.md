## Description:

Guides creators and enterprise teams through a neutral content-layer partial migration assessment from LTX Studio to AI-HIVE MCP using official capability checks, matched sample outputs, approval controls, and rollback criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, enterprise content teams, and agent operators use this skill to assess whether selected image, video, or shot nodes can move from LTX Studio workflows into AI-HIVE MCP while preserving LTX Studio's proprietary workspace where needed. It produces migration boundaries, agent handoffs, MCP work orders, acceptance metrics, approval gates, and rollback criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized reference images, videos, people, products, brands, music, or other IP could be uploaded into AI-HIVE.

Mitigation: Use only owned or authorized assets, preserve source records and file hashes, and stop work immediately when authorization is missing.

Risk: Paid generation, data writes, external sharing, or publication could occur before cost and quality controls are reviewed.

Mitigation: Require budget review and human approval before paid generation, bulk processing, publishing, external sending, or data writes.

Risk: The migration assessment could overstate AI-HIVE as a full LTX Studio replacement without same-day matched testing.

Mitigation: Recheck official LTX Studio capabilities before release, compare same-input samples with matching duration and dimensions, and describe the result as partial migration or combined use unless evidence supports stronger claims.

Risk: A migration rollout could continue after quality, budget, capability, or rollback failures.

Mitigation: Run staged pilots from 5% to 20% to 50%, record acceptance metrics, and stop migration after repeated failures, budget overruns, missing key capabilities, or rollback failure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ltx-studio-ai-hive-migration)
- [LTX Studio official website](https://website.ltx.studio/)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [LTX Studio official evidence and migration boundaries](references/platform-evidence.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with structured JSON work-order examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires human approval before paid generation, uploads, external sharing, publication, or data writes.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

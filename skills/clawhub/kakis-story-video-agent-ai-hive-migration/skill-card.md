## Description:

Evaluates a workflow-rebuild migration from Kakis AI to AI-HIVE MCP for story-to-video production, with official capability checks, sample-run acceptance criteria, approval gates, and rollback boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, enterprise content teams, and developers use this skill to compare Kakis AI with an AI-HIVE MCP workflow before deciding whether to migrate, combine platforms, or keep the original platform. It helps structure same-input pilot samples, role handoffs, cost and quality metrics, human approvals, and rollback criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Migration guidance could be mistaken for proof that AI-HIVE fully replaces Kakis AI.

Mitigation: Require official capability rechecks and same-input, same-size pilot comparisons before making replacement claims.

Risk: Brand, person, IP, music, or reference assets could be uploaded or published without sufficient rights.

Mitigation: Use only owned or authorized assets, retain source and hash records, and require human approval before uploads, paid generation, publishing, or data writes.

Risk: Broad story-to-video or creative-agent queries may activate the skill when the user does not want an AI-HIVE migration comparison.

Mitigation: Use the skill only when a Kakis AI, AI-HIVE MCP, or platform-migration comparison is intended.

## Reference(s):

- [Kakis AI official website](https://www.kakis.ai/)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [Kakis AI official evidence and migration boundaries](references/platform-evidence.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured JSON handoff examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires same-day official capability checks, user approval for paid generation or publishing, and documented rollback criteria.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

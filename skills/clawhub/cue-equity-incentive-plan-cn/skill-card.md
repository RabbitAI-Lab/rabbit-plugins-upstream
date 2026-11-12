## Description:

Turns an A-share equity incentive plan draft or related announcement into eight clause cards with verbatim quotes and source anchors, while leaving financial estimates and investment judgments for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and analysts use the skill to extract the stated terms from a China A-share incentive plan, including award type, quantity, recipients, pricing, vesting and exercise conditions, special cases, and approval and disclosure steps. It preserves source wording and anchors so readers can check the draft directly.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: ClawScan flags undeclared service-discovery behavior, unsafe handling of a routing credential, and unpinned installation sources; its scan coverage was partial.

Mitigation: Before installation, review the service-discovery and external-parsing behavior, independently verify where CUE_API_KEY is sent, and pin the installer and source to reviewed versions.

## Reference(s):

- [EIP terms reference](references/eip-terms.md)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)
- [Cue MCP setup](https://cuecue.cn/hub/mcp)
- [Cue Omni Reader setup](https://cuecue.cn/hub/omni-reader)
- [Cue API key information](https://cuecue.cn/hub/api-key)
- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-equity-incentive-plan-cn)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown with eight clause entries, verbatim excerpts, source anchors, missing-item notes, and a human-review section]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One plan per card; financial estimates and investment judgments are marked [待人工].]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

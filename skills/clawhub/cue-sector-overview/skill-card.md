## Description:

按指定行业与时间窗生成六节 A 股行业景气证据报告，附可比序列锚、代表公司清单和覆盖缺口；不提供行业观点或荐股择时。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

供投研人员用于行业开题、会前准备和尽调章节。提供行业名称与时间窗后，整理行业冷热证据、来源锚点、代表 A 股公司和覆盖缺口。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connection examples may expose the Cue API key beyond the intended destination.

Mitigation: Use the documented user-supplied-material route without a Cue key until credential handling is fixed.

Risk: Authenticated requests to an unapproved endpoint or unsafe redirect can disclose credentials.

Mitigation: Before enabling authenticated connectivity, require HTTPS and approved-host checks in every example, and disable redirects or validate them safely.

Risk: Generated report evidence may be incomplete or require independent confirmation.

Mitigation: Independently verify report evidence and review optional external skills and live service behavior separately.

## Reference(s):

- [Cue data configuration](https://cuecue.cn/hub/mcp)
- [Cue Omni Reader configuration](https://cuecue.cn/hub/omni-reader)
- [Cue API key setup](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Files, Guidance]

**Output Format:** [Six-section Markdown sector report with supporting industry materials, source index, and run log]

**Output Parameters:** [Industry and reporting window]

**Other Properties Related to Output:** [Evidence-linked sector conditions, representative A-share companies, and declared coverage gaps; no stock picks or market-timing advice.]

## Skill Version(s):

0.1.34 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

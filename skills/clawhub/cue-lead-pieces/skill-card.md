## Description:

帮助分析人员从公司公开披露中整理信用风险线索，并将引文与所标注页码附近的原文逐字核对。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT

## Use Case:

外部分析师和研究团队可用它从公司公开披露中整理可追溯的信用风险线索，并核对引文及来源页码。它提供可核验证据，不提供投资或信贷建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unchecked source IDs or output paths could overwrite unrelated files.

Mitigation: Validate source IDs, contain output paths, and use a restricted workspace without write access to unrelated files.

Risk: Redirects on credential-bearing requests could expose an API key.

Mitigation: Reject redirects or revalidate every destination before forwarding authorization.

Risk: Optional Cue or model services may receive filing URLs or excerpts; parsing or research may incur charges, and repaired quotes may still need contextual review.

Mitigation: Obtain approval before paid operations and review repaired quotes against their surrounding source text.

## Reference(s):

- [ClawHub release](https://clawhub.ai/huhoo/skills/cue-lead-pieces)
- [Verification guide](references/verification.md)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)
- [Cue service](https://cuecue.cn)
- [Cue API key setup](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Markdown reports and JSON records with filing references and page citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quotes are checked against source text; unsupported quotes can be flagged, restored, or dropped.]

## Skill Version(s):

0.4.32 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

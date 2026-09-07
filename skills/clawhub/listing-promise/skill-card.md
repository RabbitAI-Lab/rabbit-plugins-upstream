## Description:

核对 Amazon Listing 中的功能、效果和使用承诺与评论反馈是否一致，并标出证据缺口；需要 ARI API key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operations teams use this skill to compare listing promises against collected review evidence, identify evidence gaps, and decide whether to proceed with paid ARI listing/promise analysis after quote confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the skill exposes paid, persistent account-management and broader Amazon operations features beyond its narrow listing-promise description.

Mitigation: Install only if granting an ARI API key is acceptable, keep autoconfirm set to ask when per-action control is needed, and review quotes before confirming paid analysis.

Risk: Prompts or workflows can lead to recurring monitoring, competitor tracking, exports, or paid reports.

Mitigation: Use explicit only-quote wording for pricing checks and require clear user confirmation before paid reports, monitoring changes, competitor tracking, or exports.

Risk: Results depend on available ARI product-detail and review data and may not cover every variant, site, or current Amazon state.

Mitigation: State ASIN, site, sample size, time window, and evidence gaps; avoid legal compliance conclusions, unsupported marketing claims, or automatic listing changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/listing-promise)
- [Amazon Listing 承诺核查 README](README.md)
- [Dedicated listing/promise workflow](references/operation-workflow.md)
- [ARI CLI and API reference](references/reference.md)
- [ARI user guide](使用说明.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report text with optional shell command snippets and ARI report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include ASIN, site, data range, sample limits, evidence gaps, credit usage when available, and clear separation between data, inference, and recommendations.]

## Skill Version(s):

1.4.7 (source: server release, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

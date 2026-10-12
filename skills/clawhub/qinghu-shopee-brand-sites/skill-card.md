## Description:

查询品牌在 Shopee 各站点近 30 天的销量、销售额及占比，帮助比较品牌在不同国家站点的表现。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee 品牌运营人员和分析人员使用此技能比较品牌在不同国家站点的近 30 天销售表现与份额，识别表现较强的站点。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation or upgrade of unpinned external tooling may change the host environment or introduce unreviewed code.

Mitigation: Preinstall a reviewed, pinned qhkit version and review any Node/npm installation before allowing environment changes.

Risk: Saving the qhkit API token persistently on the host increases credential exposure.

Mitigation: Prefer an ephemeral QHKIT_TOKEN and avoid persisting the token through qhkit configuration.

Risk: Paid data queries may consume Qinghu credits, including on some failed calls.

Mitigation: Check the current price and get user approval before paid calls; avoid repeated speculative retries and report actual credits used.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-brand-sites)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown analysis, with a table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports site-level sales, revenue and shares for the queried 30-day period; results depend on the external data service.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

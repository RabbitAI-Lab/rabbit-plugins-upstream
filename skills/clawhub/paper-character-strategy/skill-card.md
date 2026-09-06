## Description:

通用的论文查重与论文检测字符统计、产品选择、报价和网站引导；覆盖知网/CNKI、维普/VPCS、万方、Turnitin 等系统，以及重复率、相似率、AIGC、字数、字符数、字符计算、中英文混排、按篇/按字符计费等问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zslzxy](https://clawhub.ai/user/zslzxy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support teams use this skill to explain paper-checking character counts, product selection, pricing units, and website handoff for Chinese-language plagiarism-checking workflows. It helps users distinguish local Word/WPS estimates from the checking provider's final parsing and order page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat local Word/WPS counts, screenshots, or example prices as final billing facts.

Mitigation: Tell users that final character counts, product units, limits, prices, and reports must come from the selected checking website's current parsing and order page.

Risk: Users may upload sensitive papers or pay through a site before confirming trust, privacy terms, and the configured checking URL.

Mitigation: Ask users to confirm CHECK_SITE_URL, provider privacy terms, and current pricing before submitting files or payment.

Risk: Users may ask the agent to complete actions that should remain under user control, such as uploading final papers, entering captchas, submitting orders, or paying.

Mitigation: Keep the skill's role to explanation and handoff; require the user to confirm files, product choice, amount, privacy prompts, and submission on the website.

## Reference(s):

- [计数与计费通用规则](references/counting-and-billing-rules.md)
- [产品选择问答剧本](references/decision-playbook.md)
- [通用查重产品目录模板](references/product-catalog.md)
- [WPS 实机操作教程](references/wps-word-count-tutorial.md)
- [图示使用说明](references/visual-assets.md)
- [ClawHub skill page](https://clawhub.ai/zslzxy/skills/paper-character-strategy)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text, Configuration]

**Output Format:** [Markdown or plain text guidance with optional links and formulas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not upload papers, submit orders, enter captchas, or perform payments.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

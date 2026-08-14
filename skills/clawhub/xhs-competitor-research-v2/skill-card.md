## Description:

当用户需要做小红书竞品研究、小红书竞品分析、同赛道观察、内容角度对比、内容策略对比或品牌内容调研时使用。面向品牌、MCN、内容运营和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, MCN, content operations, and creator teams use this skill to search Xiaohongshu by keyword or topic direction, compare competitor content angles, and organize visible samples into research findings and follow-up questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Returned XHS note links can include xsec_token values that function as sensitive share links.

Mitigation: Treat tokenized result links as sensitive and share or store them only where appropriate.

Risk: API error responses may include recharge or billing links.

Mitigation: Verify any recharge or billing URL is on the official SocialDataX domain before opening it or paying.

Risk: The skill runs an npm CLI with a SocialDataX API key from the user's environment.

Mitigation: Install only when comfortable using SocialDataX with SOCIALDATAX_API_KEY and keep the key in environment configuration rather than generated files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-competitor-research-v2)
- [SocialDataX AI access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash commands and structured search-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY plus node/npm; supports read-only XHS search, pagination, optional filters, and sample-based follow-up analysis.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

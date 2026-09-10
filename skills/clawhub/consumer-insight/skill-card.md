## Description:

亚马逊消费者洞察 Skill 生成深度 Amazon 评论洞察报告，覆盖用户画像、购买动因、使用场景、痛点与未满足需求、竞品替代关系和改进机会，并将结论回溯到具体评论证据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, operators, and market researchers use this skill to turn ASIN review data into concise or full consumer insight reports for product decisions, listing improvements, competitor comparison, and market presentations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits, including through documented auto-confirm behavior.

Mitigation: Set auto-confirm off or use quote-only wording before paid work, and require explicit confirmation before running paid analyses when cost control matters.

Risk: The skill can change ongoing account settings such as recurring collection or monitoring.

Mitigation: Review any request to enable weekly or daily collection, recurring monitoring, or account automation before approving it.

Risk: The skill requires an ARI API key and performs account actions through ARI.

Mitigation: Use the documented authorization flow or environment variable, avoid sharing the key in chat or reports, and revoke or rotate the key if exposure is suspected.

Risk: Custom ARI endpoint settings can redirect requests away from the official service.

Mitigation: Avoid custom ARI_BASE_URL settings unless you control the endpoint and have verified that it uses safe transport.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/consumer-insight)
- [README](README.md)
- [使用说明](使用说明.md)
- [ARI API Reference](references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and concise text summaries with occasional inline shell commands for setup or troubleshooting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include sampled review evidence, report links, exported Markdown or HTML availability, account credit use, and data-range caveats.]

## Skill Version(s):

1.4.8 (source: frontmatter, changelog, release evidence, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

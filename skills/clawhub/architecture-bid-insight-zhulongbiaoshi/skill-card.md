## Description:

建筑工程标讯洞察-筑龙标事 helps building-industry users search construction bids, track infrastructure and large-project opportunities, analyze companies and markets, and identify likely bidders using Zhiliaobiaoxun data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External construction, procurement, sales, and market-analysis users use this skill to find bid opportunities, monitor project timelines, research companies, compare competitors, identify potential suppliers, and summarize market trends from public bidding data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic onboarding can collect device characteristics and create local API-key state.

Mitigation: Prefer manually setting ZLBX_API_KEY; approve automatic registration only after reviewing the disclosed platform, CPU architecture, and MAC-derived hash collection.

Risk: API keys and account information may be exposed if copied into chat or mishandled locally.

Mitigation: Keep keys in the environment or local agent configuration, avoid displaying API keys in responses, and protect the local configuration file.

Risk: Returned company contact data can be sensitive and may be masked depending on account tier.

Mitigation: Use returned contact data only as provided, do not attempt to recover masked contact details, and avoid bulk exporting contacts.

Risk: Related next-step links may include referral or tracking parameters.

Mitigation: Show only contextually relevant links and make clear when they are optional follow-up actions.

## Reference(s):

- [ClawHub Release Page](https://clawhub.ai/pkuycl/skills/architecture-bid-insight-zhulongbiaoshi)
- [Bid Search API Details](references/api-search.md)
- [Company Analysis API Details](references/api-company.md)
- [Market Analysis API Details](references/api-market.md)
- [Account Query API Details](references/api-account.md)
- [Automatic Registration Flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with tables, summaries, links, request examples, and occasional shell commands or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY for normal use; account tier can affect contact visibility.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes a named public-market industry chain with Cue to map upstream, midstream, and downstream participants, explain demand transmission, surface less-covered A-share segment leaders, and produce risk-aware source-linked research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External investors, analysts, and industry researchers use this skill to turn a named industry chain into a structured Cue research report covering chain map, transmission logic, candidate hidden champions, elasticity assessment, risks, and source links. It is intended for public A-share fundamental research, not trading instructions or private company intelligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses Cue as a third-party research service and may send the user's query and API key to cuecue.cn.

Mitigation: Use only for queries appropriate for that service, avoid sensitive unpublished research prompts, and review Cue account and API-key handling before installation.

Risk: Generated industry-chain and stock research may be incomplete, stale, or misleading if Cue or public data sources are unavailable or wrong.

Mitigation: Treat outputs as research support, verify cited public sources independently, and do not use the skill as direct buy, sell, or timing advice.

Risk: The artifact behavior encourages Cue share links and referral or recharge messaging beyond the core research task.

Mitigation: For sensitive reports, tell the agent not to include a Cue share link, and treat referral or recharge guidance as platform promotion rather than research output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/panting09266-ai/skills/cue-supply-chain-mining)
- [Publisher Profile](https://clawhub.ai/user/panting09266-ai)
- [Cue Platform](https://cuecue.cn/)
- [Cue API Key Management](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown research report with source links and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a Cue share link and local report path when available; report quality depends on Cue and public data sources.]

## Skill Version(s):

1.1.5 (source: server release metadata; artifact frontmatter lists 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

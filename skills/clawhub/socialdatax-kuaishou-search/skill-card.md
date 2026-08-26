## Description:

用于快手数据分析、快手作品研究、关键词观察、内容调研、竞品分析和趋势研究。覆盖 Kuaishou / Kwai work research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Kuaishou/Kwai works through SocialDataX for keyword observation, content research, competitor analysis, and trend scanning. It helps agents run the documented CLI or available MCP tool and summarize visible result evidence separately from interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SOCIALDATAX_API_KEY and sends Kuaishou search terms to SocialDataX.

Mitigation: Install and use it only when that API-key use and data sharing path are acceptable; keep the API key in the environment and avoid exposing it in outputs.

Risk: Examples may run the socialdatax-skills npm package through npx.

Mitigation: Use normal npm package provenance checks and execution controls before running the CLI in sensitive environments.

Risk: Kuaishou search pagination uses opaque next_page_token values that can break if modified.

Mitigation: Pass returned pagination tokens back unchanged within the same search chain and avoid truncating, masking, or rebuilding them.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-search)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Analysis]

**Output Format:** [Markdown guidance with shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search result summaries may include Kuaishou photo IDs, share URLs, author facts, visible interaction counts, and publish times when traceability is useful.]

## Skill Version(s):

0.1.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

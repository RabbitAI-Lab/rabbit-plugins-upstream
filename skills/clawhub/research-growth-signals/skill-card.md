## Description:

Research traceable public social and SEO signals through SignalDig's single MCP connection and two business tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research bounded public social discussions and SEO evidence through SignalDig, including keyword demand, SERP signals, trends, competitors, GEO visibility, backlinks, rankings, traffic, and public social posts. The skill helps an agent choose the smallest useful Social or SEO scope, poll work to a terminal state, and report coverage, limitations, and source analysis IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may send social or SEO research queries, domains, keywords, platform selections, or public profile URLs to SignalDig through its MCP service.

Mitigation: Confirm that the SignalDig account and data handling are acceptable before use, and avoid private or sensitive material unless the user trusts SignalDig for that data.

Risk: If SignalDig is unavailable, disconnected, or authentication fails, the agent could otherwise fabricate research results.

Mitigation: Stop instead of simulating results, tell the user SignalDig is not connected, and direct them to the SignalDig setup link.

Risk: Partial coverage, unsupported constraints, or source limits could be mistaken for exhaustive market evidence.

Mitigation: Report actual coverage and limitations from terminal SignalDig responses, and avoid describing partial evidence as exhaustive or representative.

## Reference(s):

- [SignalDig Homepage](https://signaldig.com/)
- [Connect SignalDig](https://signaldig.com/agent-setup)
- [SignalDig ClawHub Skill](https://clawhub.ai/jerrykik/skills/research-growth-signals)
- [SignalDig Unified Research MCP Contract](references/mcp-contract.md)
- [SignalDig Connection Setup](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Concise text or Markdown with cited public evidence, coverage, limitations, and analysis IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded MCP research requests, terminal status summaries, paginated result summaries, and setup guidance when SignalDig is not connected]

## Skill Version(s):

2.1.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

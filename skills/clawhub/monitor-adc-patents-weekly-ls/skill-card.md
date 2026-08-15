## Description:

Create an evidence-backed weekly monitor of newly published antibody-drug conjugate (ADC) patent applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users, IP teams, R&D teams, competitive-intelligence teams, and business-development teams use this skill to monitor newly published ADC patent applications for a defined week, screen out noise, and prioritize records that may warrant claim review. It supports monitoring and triage, not freedom-to-operate, infringement, validity, patentability, ownership, or clinical-efficacy conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live retrieval may fail or produce incomplete coverage if the required PatSnap connectors are unavailable or unauthorized.

Mitigation: Confirm authorized access to the relevant PatSnap connectors before use; if live retrieval is unavailable, provide only the search protocol and input-gap statement.

Risk: Generated reports may expose credentials or confidential strategy details if users supply them in an unapproved environment.

Mitigation: Use an approved environment, never include API keys in reports, and limit confidential details according to organizational policy.

Risk: Patent-monitoring outputs may be mistaken for legal, clinical, or commercial conclusions.

Mitigation: Keep outputs bounded to monitoring and triage; route FTO, infringement, validity, patentability, ownership, and clinical-efficacy questions to qualified reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/monitor-adc-patents-weekly-ls)
- [PatSnap patent search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap patent briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [PatSnap current awareness MCP server](https://open.patsnap.com/marketplace/mcp-servers/current-awareness)
- [PatSnap drug asset MCP server](https://open.patsnap.com/marketplace/mcp-servers/drug-asset)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown report by default, with optional self-contained HTML when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes search protocol, screening funnel, evidence records, exclusions, limitations, source appendix, and bounded analyst interpretation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

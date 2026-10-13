## Description:

Uses Cue to identify a named company's customers and suppliers, prioritize sales prospects, and suggest possible financial-service needs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Corporate banking relationship managers use this skill to find prospective customers and suppliers around a specified company, with suggested outreach angles and potential financing needs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill executes an externally maintained runner that may change between uses and uses a Cue API key.

Mitigation: Review and pin a trusted runner version before execution, and keep the API key under the user's control.

Risk: Prospecting queries and company information are sent to Cue and external data sources.

Mitigation: Avoid confidential or regulated data unless organizational policy permits sharing it with those services.

Risk: Suggested relationships and financial needs may be incomplete or inaccurate.

Mitigation: Verify material claims against cited sources before contacting prospects or making financial decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-supply-chain-prospecting)
- [Cue platform](https://cuecue.cn)
- [Cue runner referenced by the skill (not verified import provenance)](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown report and link to the original Cue report when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prioritized prospect list, relationship evidence, suggested outreach angles, possible financial needs, and source links.]

## Skill Version(s):

1.0.7 (source: ClawHub release; supplied skill frontmatter states 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Uses Cue to map an industry supply chain, trace business-cycle transmission, identify less-followed companies, and assess potential business and valuation sensitivity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users researching companies in A-share industry chains can use this skill to build a supply-chain map, examine how business conditions may flow between segments, and identify candidates for further research.

### Deployment Geography for Use:

China (A-share markets)

## Known Risks and Mitigations:

Risk: Setup updates executable runner code without pinning a revision.

Mitigation: Pin the runner to a specific revision and review updates separately before approving them.

Risk: The skill gives conflicting instructions about protecting the API key.

Mitigation: Configure the API key locally rather than pasting it into chat.

Risk: Research uses Cue services that may process queries, consume credits, or host reports.

Mitigation: Review Cue's handling of queries, credit usage, and hosted reports before running research.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-supply-chain-mining)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown research report with supply-chain maps, analysis, risk notes, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links and a Cue report link when available.]

## Skill Version(s):

1.1.7 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

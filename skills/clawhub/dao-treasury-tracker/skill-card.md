## Description:

Tracks DAO and crypto protocol treasury composition using the free DeFiLlama treasury API, computing what percentage of a treasury is held in the project's own governance token versus diversified assets like stablecoins and ETH.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ssidharhubble](https://clawhub.ai/user/ssidharhubble)

### License/Terms of Use:

MIT-0

## Use Case:

External users, DAO analysts, DeFi researchers, and protocol reviewers use this skill to compare treasury concentration across DeFiLlama-tracked protocols and identify whether reported treasury value is diversified or mostly the protocol's own token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts DeFiLlama over the network for each requested protocol slug.

Mitigation: Run it only where outbound access to the public DeFiLlama API is acceptable, and treat network failures or API errors as data availability issues.

Risk: Treasury results are snapshots from an external data source and can be incomplete or change over time.

Mitigation: Verify material decisions against current primary sources and do not treat the output as financial advice.

Risk: Some protocols are not covered by DeFiLlama's treasury module and may return skipped errors.

Mitigation: Interpret skipped slugs as missing coverage or lookup errors, not as proof that a protocol lacks treasury assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/dao-treasury-tracker)
- [DeFiLlama treasury API](https://api.llama.fi/treasury/{slug})
- [DeFiLlama protocols API](https://api.llama.fi/protocols)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain-text table or JSON emitted by a Python command-line script, with agent guidance in Markdown when explaining results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs total treasury USD value, own-token concentration percentage, risk label, chains, and per-slug errors for unavailable treasury data.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Scores public crypto wallet activity across Ethereum, Arbitrum, Base, Optimism, and Polygon against generic retroactive airdrop heuristics and returns a 0-100 eligibility health score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ssidharhubble](https://clawhub.ai/user/ssidharhubble)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to check whether one or more public wallet addresses show enough multi-chain activity to look healthy under common airdrop-farming heuristics. It is a directional health check, not a guarantee of eligibility for any specific airdrop.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public wallet addresses checked with the tool are sent to publicnode.com RPC endpoints.

Mitigation: Use only public addresses you are comfortable querying through third-party public RPC infrastructure; never provide private keys or seed phrases.

Risk: The score is based on generic heuristics and cannot reflect unpublished snapshot rules, sybil filters, social requirements, governance votes, or protocol-specific interactions.

Mitigation: Treat the result as a directional activity signal and verify project-specific eligibility criteria before making financial or operational decisions.

Risk: Public RPC endpoint availability or transient errors can affect reported chain snapshots.

Mitigation: Review per-chain error output and rerun checks when endpoints fail before comparing wallets or acting on a score.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/airdrop-eligibility-tracker)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [CLI text report or JSON, with Markdown guidance and shell command examples for agent responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May compare multiple wallet addresses side by side; network queries are read-only and use public JSON-RPC endpoints.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

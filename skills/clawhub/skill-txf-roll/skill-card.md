## Description:

Guides agents in retrieving Blave market data and researching or executing trades through supported exchange APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Traders, researchers, and developers use this skill to analyze crypto and Taiwan market data, build trading workflows, and prepare exchange orders with explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to download and run remote Python strategies without a clear approval or isolation boundary.

Mitigation: Review strategy code first and run it only in a sandbox without inherited exchange credentials or broad filesystem access.

Risk: Financial API credentials and trading access could expose funds or sensitive account data.

Mitigation: Use least-privilege, preferably read-only keys for research; disable withdrawals and enable IP allowlisting.

Risk: Exchange orders and transfers can cause financial loss.

Mitigation: Require explicit confirmation for each order, cancellation, transfer, or funding action and check its outcome.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/blave-wei/skills/skill-txf-roll)
- [Blave documentation](https://blave.org/docs/en)
- [Blave homepage](https://blave.org)
- [Blave API reference](artifact/references/blave-api.md)
- [Exchange trading references](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Code, Shell commands]

**Output Format:** [Text or Markdown with API examples and trading instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authenticated market-data requests and exchange actions; trading actions require explicit confirmation.]

## Skill Version(s):

1.23.17 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

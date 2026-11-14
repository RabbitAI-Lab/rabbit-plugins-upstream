## Description:

Submit an observed physical or digital problem to CleanApp for private review, or check its receipt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[borisolver](https://clawhub.ai/user/borisolver)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use the skill to prepare and submit a user-approved observation of a hazard, access barrier, waste, broken infrastructure, software bug, scam, or service failure, then check its private intake receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports medium confidence and incomplete reference coverage, leaving uncertainty about the skill's tool scope and the information it may send over the network.

Mitigation: Review the skill's network destinations and sent fields before installing; use the offline preview to inspect report content before any submission.

Risk: A submitted description and optional report context leave the user's environment, and the private receipt file contains a bearer tracking token.

Mitigation: Submit only the approved report content, omit unneeded or unapproved context, and keep the receipt file private.

## Reference(s):

- [CleanApp agent onboarding](https://www.cleanapp.io/agents)
- [CleanApp agent intake API reference](references/API_REFERENCE.md)
- [CleanApp MCP server](https://live.cleanapp.io/openai/mcp)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Factual report preview and JSON receipt or status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A report is submitted only after approval; receipts remain private and confirm intake status only.]

## Skill Version(s):

0.2.0 (source: manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

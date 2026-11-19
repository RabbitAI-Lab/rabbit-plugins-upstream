## Description:

Discover your supporter personality, get personalized AI tool recommendations, connect with early supporters, and search for skills that match how you work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bloomprotocol](https://clawhub.ai/user/bloomprotocol)

### License/Terms of Use:

MIT

## Use Case:

External users, indie developers, AI builders, and ClawHub skill users use this skill to analyze recent conversation context and generate a Bloom supporter identity card with archetype, categories, tool recommendations, and a shareable dashboard link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can download and run unpinned external GitHub and npm code.

Mitigation: Review or pin the external repository and dependencies before installation, and run only from sources you trust.

Risk: The skill reads local OpenClaw session transcripts to analyze recent conversation history.

Mitigation: Use it only with conversations you are comfortable analyzing, and avoid sensitive sessions until session selection and data flow are clear.

Risk: The skill creates persistent local configuration and may use a default JWT secret.

Mitigation: Review the generated configuration and replace the default JWT secret before regular use.

Risk: Derived identity results are sent to Bloom services for the dashboard and future features.

Mitigation: Share only if you are comfortable storing the derived identity card, categories, wallet address, and dashboard URL with Bloom services.

Risk: The optional Base-network agent wallet is not ready for withdrawals or active tipping.

Mitigation: Do not deposit funds into the generated wallet until withdrawal and tipping support is explicitly available.

## Reference(s):

- [Bloom Supporter Identity on ClawHub](https://clawhub.ai/bloomprotocol/skills/bloom)
- [Bloom Protocol](https://bloomprotocol.ai)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured text with a shareable dashboard URL, identity summary, recommendation list, and optional wallet status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and npx; output may include supporter type, tagline, categories, 2x2 dimensions, tool recommendations, dashboard URL, and agent wallet status.]

## Skill Version(s):

2.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

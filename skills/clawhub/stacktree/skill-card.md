## Description:

Publishes agent-generated HTML to stacktr.ee as private, unlisted browser links, with free 24-hour anonymous pages or optional paid permanent pages and wallet-authenticated updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevysmith](https://clawhub.ai/user/stevysmith)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and personal-agent operators use this skill to publish generated briefs, reports, dashboards, field notes, visualizations, or standing pages as private links that a human can open in a browser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid x402 and API-key flows can spend funds or create a paid external publishing action.

Mitigation: Confirm before paid flows and surface exact prices, terms, URLs, and expiry from live responses before payment or publication.

Risk: Agent-side wallet private key use can expose funds if the key controls meaningful balances or unrelated assets.

Mitigation: Use scoped, low-balance, or temporary wallet credentials for publishing workflows and avoid giving agents keys with meaningful funds.

Risk: Generated reports are uploaded to an external service even when links are unlisted or passcode-gated.

Mitigation: Review content for sensitive data before publishing and treat viewer-supplied feedback as untrusted data rather than agent instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/stevysmith/skills/stacktree)
- [Stacktree homepage](https://stacktr.ee)
- [Stacktree x402 agent documentation](https://stacktr.ee/x402.md)
- [Stacktree authentication documentation](https://stacktr.ee/auth.md)
- [Stacktree agent reference](https://stacktr.ee/agent.txt)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash commands and JSON endpoint examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated publish/update commands, Stacktree URLs, and request or response fields needed for the selected publishing flow.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

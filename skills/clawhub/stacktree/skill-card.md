## Description:

Helps agents publish and update HTML pages as private links for briefs, reports, dashboards, and other shareable content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevysmith](https://clawhub.ai/user/stevysmith)

### License/Terms of Use:

MIT-0

## Use Case:

Personal agents and their users publish HTML briefs, reports, and dashboards to shareable links, then update or remove pages as needed. They can choose temporary free hosting or paid permanent hosting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing sensitive content or sending an owner's email address may disclose information.

Mitigation: Confirm the content and obtain permission before uploading a sensitive page or sending an email address.

Risk: Claim tokens, receipt links, API keys, and wallet private keys can grant access to pages or a funded wallet.

Mitigation: Keep credentials out of chats and logs; store them securely and prefer claim-token updates over exposing a wallet key.

Risk: Paid publishing or key provisioning spends USDC; deleting an unclaimed page can be irreversible.

Mitigation: Confirm the price and recipient before payment, and obtain approval before provisioning a key or deleting a page.

Risk: The optional update helper installs a dependency without an exact version pin.

Mitigation: Pin and review dependencies before using the helper, or use the claim-token curl flow instead.

## Reference(s):

- [Stacktree skill on ClawHub](https://clawhub.ai/stevysmith/skills/stacktree)
- [Stacktree x402 publishing guide](https://stacktr.ee/x402.md)
- [Stacktree authentication guide](https://stacktr.ee/auth.md)
- [Stacktree agent reference](https://stacktr.ee/agent.txt)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Links]

**Output Format:** [Markdown with HTML examples, shell commands, and page links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Published pages return a shareable URL; responses may include an expiry, claim link, and update credential.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

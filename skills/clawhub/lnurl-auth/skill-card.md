## Description:

Authenticate to LNURL-auth (LUD-04) services without a wallet, node, or payment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dyegolara](https://clawhub.ai/user/dyegolara)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to authenticate to services that present Sign in with Lightning LNURL-auth challenges. It is for authentication only and does not create invoices, make payments, or require a Lightning node or wallet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication callback data may be sent over plain HTTP.

Mitigation: Prefer HTTPS LNURL-auth challenges and avoid plain HTTP callbacks except for local testing where interception is not a concern.

Risk: A submitted challenge authenticates the user to the decoded service.

Mitigation: Run the helper with --dry-run and inspect the decoded service and callback URL before submitting authentication.

Risk: The persistent master secret controls derived linking keys.

Mitigation: Store the master secret in a protected key file, keep file permissions restricted, and never print, paste, or send the secret.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dyegolara/skills/lnurl-auth)
- [Project homepage](https://github.com/dyegolara/lnurl-auth-agents)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, text]

**Output Format:** [Markdown guidance with shell commands; helper output can be JSON or text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include decoded service URL, domain, k1 challenge, linking public key, callback URL, HTTP status, and service response.]

## Skill Version(s):

1.4.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

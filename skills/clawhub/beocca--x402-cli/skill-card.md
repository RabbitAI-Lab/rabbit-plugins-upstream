## Description:

A CLI skill that helps agents discover x402 services, inspect payment requirements, and make paywalled requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beocca](https://clawhub.ai/user/beocca)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use x402-CLI to discover x402-enabled services, inspect cost and payment metadata, and invoke paid endpoints from an agent workflow. It is suitable when the calling system can provide wallet controls and approval policy outside the CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can autonomously spend real cryptocurrency without built-in approval, spend limits, or service allowlists.

Mitigation: Use a fresh low-balance wallet and enforce approval, per-transaction limits, service allowlists, recipient allowlists, and monitoring in the calling agent before enabling request pay.

Risk: Payment endpoints and discovery results may be untrusted or unsuitable for the user's jurisdiction or use case.

Mitigation: Run request info first, verify amount, network, recipient, and service terms, and only allow known services where the calling system has performed due diligence.

Risk: Wallet private keys and request data can be exposed through environment handling or saved request files.

Mitigation: Use a dedicated wallet key, avoid logging or hardcoding secrets, unset credentials after use, and do not save requests that contain sensitive headers, request bodies, or responses.

## Reference(s):

- [x402-CLI ClawHub Skill Page](https://clawhub.ai/beocca/skills/x402-cli)
- [x402 Official Site](https://x402.org/)
- [x402 Documentation](https://docs.x402.org/introduction)
- [Coinbase CDP x402 Facilitator Docs](https://docs.cdp.coinbase.com/x402/introduction)
- [x402scan](https://www.x402scan.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI invocations print one JSON object to stdout; optional saved files are JSON.]

## Skill Version(s):

1.2.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

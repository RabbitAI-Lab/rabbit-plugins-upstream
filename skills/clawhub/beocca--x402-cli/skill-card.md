## Description:

A simple CLI that helps AI agents discover x402 services and make paywalled requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beocca](https://clawhub.ai/user/beocca)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to discover x402-enabled services, inspect payment requirements, and make paywalled HTTP requests from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate autonomous irreversible crypto payments.

Mitigation: Use a fresh, low-balance wallet dedicated to this skill and require external approval, service allowlists, recipient allowlists, and strict wallet funding limits before permitting request pay.

Risk: Request data and responses are saved to local JSON files by default for payment-related commands.

Mitigation: Use --no-save when requests contain credentials, private data, or other sensitive inputs.

Risk: An agent may pay an unintended, malicious, or unsuitable third-party endpoint.

Mitigation: Run request info before payment and verify the amount, network, recipient, and service output expectations before allowing request pay.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beocca/skills/x402-cli)
- [x402 Official Site](https://x402.org/)
- [x402 Documentation](https://docs.x402.org/introduction)
- [x402 GitHub Repository](https://github.com/x402-foundation/x402)
- [CDP Getting Started](https://docs.cdp.coinbase.com/get-started/overview)
- [CDP x402 Facilitator Docs](https://docs.cdp.coinbase.com/x402/introduction)
- [x402scan](https://www.x402scan.com/)
- [x402scan GitHub Repository](https://github.com/Merit-Systems/x402scan)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output contracts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands print one JSON object to stdout; request info and request pay save request and response JSON files by default unless disabled.]

## Skill Version(s):

1.2.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

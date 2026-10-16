## Description:

Measures x402 endpoint discoverability, registry demand, live payment challenges, and seller manifests before recommending changes to pricing or listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[33ai-wq](https://clawhub.ai/user/33ai-wq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and x402 sellers use this skill to measure whether paid endpoints are discoverable and buyable, then prioritize evidence-backed changes to listings, prices, and manifests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market probes contact public x402 discovery services and, if explicitly enabled, third-party seller endpoints.

Mitigation: Review target hosts before running; use --allow-any-host only when third-party probes are intended.

Risk: Measurement reports can contain seller URLs and be written to an unintended location.

Mitigation: Review the --out path before running and handle local reports appropriately.

## Reference(s):

- [x402-market-recon release](https://clawhub.ai/33ai-wq/skills/x402-market-recon)
- [Decision rules and thresholds](references/decision-rules.md)
- [Dated market baseline](references/findings-baseline.md)
- [Coinbase x402 discovery registry](https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Written analysis and local JSON/JSONL measurement reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are written under --out (default ./recon); no payment is made.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Measures x402 registry demand, live payment-challenge responses, and seller discovery manifests before changes to listings or payment paths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[33ai-wq](https://clawhub.ai/user/33ai-wq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and x402 sellers use this skill to measure discoverability, demand, pricing constraints, and live payment terms before deciding whether to change an endpoint or listing. It produces a dated, sourced report and identifies unverified findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Probing seller endpoints can contact third-party public hosts.

Mitigation: Review the destinations and opt in explicitly before allowing off-domain HTTPS reads.

Risk: Registry figures and probe reports may be incomplete or misleading when used to change prices or listings.

Mitigation: Re-measure current conditions and review the generated reports before changing a payment path or listing.

## Reference(s):

- [ClawHub x402-market-recon release](https://clawhub.ai/33ai-wq/skills/x402-market-recon)
- [Decision rules and thresholds](references/decision-rules.md)
- [Dated market findings baseline](references/findings-baseline.md)
- [Coinbase x402 discovery registry](https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Written analysis with local JSON and JSONL measurement reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include measured sources, dates, sample sizes, and unverified findings; local files are written under the selected output directory.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

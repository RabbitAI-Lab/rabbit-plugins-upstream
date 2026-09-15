## Description:

Generates an evidence-based weekly comparison report for a primary Amazon ASIN and authorized competitor ASINs after quote review and explicit user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and marketplace analysts use this skill to compare a primary Amazon product with authorized competitor products and produce a weekly evidence report from product details, snapshots, and review samples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The operations CLI exposes --workflow and --focus overrides, which may broaden execution beyond the documented weekly competitor report flow.

Mitigation: Use the packaged weekly/competitor defaults and block or avoid --workflow and --focus overrides unless broader ARI product-operations workflows are explicitly intended.

Risk: Paid ARI collection or analysis can spend credits after confirmation.

Mitigation: Review the quote and requestId first, run paid operations only after explicit user confirmation, and use status checks instead of rerunning confirmed requests after interruptions.

Risk: The skill requires an ARI account and API key.

Mitigation: Configure credentials through the documented setup or configure commands, avoid sharing API keys in prompts or logs, and verify account status with check before use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/competitor-weekly)
- [Amazon competitor weekly workflow](artifact/references/operation-workflow.md)
- [Amazon competitor weekly API reference](artifact/references/reference.md)
- [ARI service endpoint](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid collection or analysis.]

## Skill Version(s):

1.4.11 (source: server release metadata, artifact _meta.json, CHANGELOG, CLI VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

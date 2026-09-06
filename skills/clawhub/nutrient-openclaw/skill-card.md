## Description:

Use the pinned Nutrient OpenClaw plugin to convert, OCR, extract, redact, watermark, sign, or inspect the last-known local credit record for documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jdrhyne](https://clawhub.ai/user/jdrhyne)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document-workflow operators use this skill in OpenClaw to route document conversion, OCR, extraction, redaction, watermarking, signing, and credit-ledger checks through the pinned Nutrient OpenClaw plugin with explicit confirmation before any credit-consuming hosted processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents or pages may be uploaded to Nutrient DWS and consume credits.

Mitigation: Before each processing call, disclose the transfer, provide a numeric or bounded credit estimate from official pricing, and require a fresh yes/no confirmation for that exact call.

Risk: The Nutrient API key could be exposed if handled in chat, commands, logs, or plaintext configuration.

Mitigation: Use the protected OpenClaw settings or secrets flow, validate the binding in the installed runtime, and verify readiness only from redacted status and tool availability.

Risk: AI redaction and signing outputs can be incomplete, overbroad, or insufficient for legal and operational requirements.

Mitigation: Preserve source files, treat AI-redaction outputs as candidates, require human review of affected pages, and route signing needs that require certificate custody, identity proofing, or regulated compliance to an approved signing workflow.

## Reference(s):

- [Reviewed plugin contract](references/plugin-contract.md)
- [Pinned plugin source](https://github.com/PSPDFKit-labs/nutrient-openclaw)
- [NPM package](https://www.npmjs.com/package/@nutrient-sdk/nutrient-openclaw)
- [OpenClaw skills](https://docs.openclaw.ai/skills)
- [OpenClaw secrets](https://docs.openclaw.ai/gateway/secrets)
- [OpenClaw tool plugins](https://docs.openclaw.ai/plugins/tool-plugins)
- [Nutrient DWS credit calculation](https://www.nutrient.io/guides/dws-processor/pricing/calculate-credit-usage/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown guidance with exact tool names, confirmation text, and configuration paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill gates credit-consuming DWS calls with bounded estimates, external-transfer disclosure, and one-call confirmation.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

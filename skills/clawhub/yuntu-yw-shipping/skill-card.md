## Description: <br>
Provides YunExpress and Yanwen cross-border shipping workflows for tracking parcels, checking orders, quoting rates, retrieving labels, and safely preparing carrier-side shipment requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvsao](https://clawhub.ai/user/lvsao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ecommerce sellers and support operators use this skill to track YunExpress or Yanwen packages, compare carrier quotes, retrieve carrier records, and prepare shipping orders or carrier changes. Write actions require merchant-approved credentials, a redacted preview, and explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Carrier credentials and shipment data may be handled by API paths that include plaintext HTTP. <br>
Mitigation: Use merchant-approved credentials only, keep environment files private and out of Git, prefer secure carrier endpoints where available, and proceed with plaintext HTTP paths only after accepting that risk. <br>
Risk: Carrier-side write operations can create, cancel, intercept, or otherwise change shipments, IOSS records, subscriptions, customs records, manifests, or CPSC submissions. <br>
Mitigation: Generate a redacted preview first and require explicit confirmation naming the operation and affected orders before executing any write. <br>
Risk: Shipment payloads can contain personal data, addresses, phone numbers, emails, and account secrets. <br>
Mitigation: Redact sensitive fields in summaries, avoid pasting secrets into chat or source files, and store local payload and environment files privately. <br>


## Reference(s): <br>
- [YunExpress Shipping API reference](references/yunexpress-api.md) <br>
- [Yanwen API reference](references/yanwen-api.md) <br>
- [Project homepage](https://github.com/lvsao/shopify-skill-hub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON-oriented request guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May summarize carrier API responses, redacted previews, validation findings, quote comparisons, tracking status, label URLs, and next-step guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

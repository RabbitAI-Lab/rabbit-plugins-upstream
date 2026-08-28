## Description:

This skill performs paid VIN lookups through Juhe Data to return vehicle make, model, powertrain, dimensions, tire, transmission, announcement number, wheelbase, and related vehicle profile details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query detailed vehicle profile and configuration data for a specific 17-character VIN, including scenarios such as vehicle verification before used-car transactions or finance and insurance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each lookup is paid and sends the VIN to Juhe over HTTPS.

Mitigation: Confirm the user understands the per-query charge and third-party VIN submission before payment or lookup.

Risk: Returned vehicle data may be delayed or incomplete and should not be the sole basis for legal, financial, insurance, or purchase decisions.

Mitigation: Present results as reference information and direct users to verify against registration records, manufacturers, or other authoritative sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-vin-query-details-a2a)
- [Juhe VIN lookup API endpoint](https://apis.juhe.cn/a2a/query)
- [Output format specification](artifact/OUT_FORMAT.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, guidance]

**Output Format:** [Markdown vehicle information report after a paid lookup, with structured tables and fallback no-record output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a valid VIN and successful Alipay-based payment; vehicle data is supplied by Juhe Data and should be treated as reference information.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

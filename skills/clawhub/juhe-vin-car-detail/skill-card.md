## Description:

Looks up vehicle factory specifications from a 17-character VIN using Juhe's VIN API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to validate a 17-character VIN and retrieve vehicle specifications from Juhe for vehicle identification, configuration checks, and second-hand car review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: VIN lookups disclose the VIN and Juhe API key to Juhe.

Mitigation: Use the JUHE_VIN_CAR_DETAIL_KEY environment variable or a protected .env file, avoid passing the key on the command line, and query only VINs the user is authorized to submit.

Risk: Juhe VIN lookups may be metered and require an approved application scenario.

Mitigation: Confirm Juhe API access approval, quota, and cost expectations before running lookups.

Risk: Lookup results can be unavailable or fail when a VIN is malformed, outside Juhe coverage, or the upstream service is unavailable.

Mitigation: Normalize and validate VINs before querying, handle documented Juhe error codes, and present unavailable results as lookup failures rather than verified vehicle facts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-vin-car-detail)
- [Juhe VIN vehicle information API documentation](https://www.juhe.cn/docs/api/id/862)
- [Juhe data service platform](https://www.juhe.cn)
- [Juhe VIN API endpoint](https://apis.juhe.cn/carinfo/vinInfo)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Plain text lookup results with a JSON response payload and Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, JUHE_VIN_CAR_DETAIL_KEY, and a valid 17-character VIN.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

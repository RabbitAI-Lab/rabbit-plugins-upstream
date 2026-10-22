## Description:

Every GTM API plan on datacircle.dev, as one file you download and query. LinkedIn profiles, people and company search, find and validate email and phone, company data, jobs and posts, each plan with its price per 1,000, score, rate limits, the fields it returns and its docs. Use it to compare or price a GTM data API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[waynehamadi](https://clawhub.ai/user/waynehamadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GTM teams use the skill to compare or price GTM data APIs by querying plans, pricing, rate limits, returned fields, and documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloading the catalog to datacircle.json may replace an existing file in the working directory.

Mitigation: Run the download in a dedicated working directory or confirm that replacing datacircle.json is acceptable.

Risk: Vendor pricing may change after the catalog is downloaded.

Mitigation: Verify current vendor pricing and documentation before purchasing.

## Reference(s):

- [DataCircle documentation](https://datacircle.dev/docs)
- [DataCircle field definitions](https://datacircle.dev/fields)
- [DataCircle catalog (JSON)](https://datacircle.dev/datacircle.json)
- [DataCircle catalog (CSV)](https://datacircle.dev/datacircle.csv)

## Skill Output:

**Output Type(s):** [Analysis, JSON, CSV, Shell commands, SQL, Guidance]

**Output Format:** [Pricing and plan comparisons with query results and shell, SQL, jq, or Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Refresh the downloaded catalog before relying on older local pricing data.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

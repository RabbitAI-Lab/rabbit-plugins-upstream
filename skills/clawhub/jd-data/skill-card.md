## Description:

Collects JD.com product details and customer reviews through a credit-based data platform, with batch collection and protection against duplicate charges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product analysts use the skill to collect JD.com product details and paginated customer reviews for product selection and review analysis. Collection uses platform credits, so users should check current prices and available balance before running batch jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Collection calls consume platform credits, and batch jobs can accumulate charges.

Mitigation: Check the live balance and interface prices before a batch, confirm the budget for jobs over 50 calls, and stop on insufficient-credit responses.

Risk: The security review reported broad activation wording, undeclared tool scope, environment-to-file-write flows, and incomplete scan evidence.

Mitigation: Limit use to requested JD product or review collection, review the requested scope and output path, and keep credentials in the documented local configuration or environment variables.

## Reference(s):

- [AI Data Platform](https://zlh.aidata366.com)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Text]

**Output Format:** [JSON API responses or saved JSON files, with text status and error messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product detail data or paginated review data; large responses can be saved to a file.]

## Skill Version(s):

1.6.6 (source: skill frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

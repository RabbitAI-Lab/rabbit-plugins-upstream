## Description:

Collects JD.com product details and customer reviews through a data API, with balance checks for batch requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to collect JD.com product details and paginated customer reviews for product selection and review analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment rates the skill suspicious because broad triggers may launch an unrelated JD data workflow; its partial scan also reports undeclared tool scope and environment-controlled file writes.

Mitigation: Review the skill's scope and granted capabilities before installation, and activate collection only for explicit JD product or review requests.

Risk: Product and review collection consumes platform points, so batch jobs can incur substantial costs.

Mitigation: Check the live balance and prices before a batch, estimate its total cost, and stop when funds or the user's budget are insufficient.

Risk: Login can save an API key in a local configuration file, and collection responses can be written to disk.

Mitigation: Keep the configuration file private, never expose the API key, and use an intentional output path for saved responses.

## Reference(s):

- [JD Data skill on ClawHub](https://clawhub.ai/cuiyunhai/skills/jd-data)
- [Data API platform](https://zlh.aidata366.com)

## Skill Output:

**Output Type(s):** [JSON data, Files, Shell commands, Configuration guidance]

**Output Format:** [JSON responses written to stdout or files, with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports paginated reviews, batch workflows, and saving large responses to files.]

## Skill Version(s):

1.6.4 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

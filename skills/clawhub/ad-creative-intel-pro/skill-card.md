## Description:

广告情报专业版 helps acquisition teams, campaign optimizers, and market researchers query ad creative intelligence APIs for bulk creative export, historical trend review, multi-market comparison, attribution workflows, and estimated download or revenue analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing, growth, and market research teams use this skill to guide API-based ad creative research, bulk data export, historical performance review, multi-market comparisons, and competitive download or revenue estimation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests shell execution plus local file read and write capabilities for API-driven workflows.

Mitigation: Review generated shell commands before execution and require explicit approval for file exports, scheduled jobs, or writes outside a chosen working directory.

Risk: The skill depends on an external ad-intelligence API and a professional API key.

Mitigation: Store the API key in an environment variable or approved secret store and avoid echoing, committing, or embedding credentials in prompts, scripts, or exported files.

Risk: Downloaded and revenue data are described as third-party estimates that may be inaccurate.

Mitigation: Label estimated values in outputs and avoid using them as the sole basis for business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ad-creative-intel-pro)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Ad Creative Intel quota endpoint](https://api.ad-creative-intel.com/api/quota/status)
- [Ad Creative Intel search endpoint](https://api.ad-creative-intel.com/api/data/search)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include API request examples, analysis workflows, troubleshooting guidance, and reminders to label third-party download and revenue estimates.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

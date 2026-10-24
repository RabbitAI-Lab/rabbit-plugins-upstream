## Description:

Analyze Amazon listings, find keyword opportunities from Amazon autocomplete, and identify competitor ASINs for seller optimization workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[avmw2025](https://clawhub.ai/user/avmw2025)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce operators, and agent users can use this skill to score product listings, research long-tail keywords, and spot competitor listing gaps. It is suited for listing-quality review and marketplace SEO research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace input can route research terms to unintended non-Amazon hosts.

Mitigation: Use ordinary marketplace values such as com or co.uk and review command arguments before execution.

Risk: Keyword and competitor research queries may reveal confidential product plans or proprietary keywords.

Mitigation: Use non-confidential research terms and avoid entering sensitive business strategy into the scripts.

Risk: Scripts save JSON reports locally and may write outside the expected reports folder if paths are changed.

Mitigation: Run the skill in a trusted workspace and inspect generated report paths before sharing or committing output.

## Reference(s):

- [Amazon Listing Optimizer on ClawHub](https://clawhub.ai/avmw2025/skills/amazon-listing-optimizer)

## Skill Output:

**Output Type(s):** [text, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and JSON report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May make network requests to Amazon domains and save local JSON reports.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact skill.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

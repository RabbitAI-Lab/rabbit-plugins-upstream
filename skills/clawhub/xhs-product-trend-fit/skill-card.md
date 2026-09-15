## Description:

Analyzes a product image and description against Xiaohongshu search results to estimate recent trend heat, choose one promotional angle, and generate a report with evidence from popular posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and product marketers use this skill before publishing Xiaohongshu notes to check whether a product category has recent traction, identify a clearer promotional direction, and review examples of high-performing posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product descriptions, local image paths, and scraped Xiaohongshu content may be sent to an LLM endpoint through the local helper.

Mitigation: Use non-sensitive product inputs and confirm WC3_LLM_ENDPOINT is unset or points only to a trusted service before running the skill.

Risk: Generated reports and temporary prompt/output files may contain product data and collected public content.

Mitigation: Store outputs in a controlled directory, review report contents before sharing, and remove temporary artifacts when the run is complete.

Risk: The workflow depends on a local Chrome relay and logged-in Xiaohongshu browser session.

Mitigation: Run it only in a trusted browser profile and verify the wc3 Chrome relay and local pipeline are expected before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fatmind/skills/xhs-product-trend-fit)
- [Publisher profile](https://clawhub.ai/user/fatmind)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [HTML report with JSON and Markdown companion files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill writes a report path, res.json, and data.md under the configured output directory, defaulting to /tmp/xhs-product-trend-fit-output.]

## Skill Version(s):

1.1.3 (source: server-resolved release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

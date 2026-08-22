## Description:

Analyzes a product image and description to identify Xiaohongshu promotion directions, recent trend heat, viral note examples, and supporting evidence in an HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing operators use this skill before promoting a product on Xiaohongshu to assess fit, recent engagement signals, and comparable viral notes. Developers can run it locally with a product image and description to generate a structured analysis report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill controls an active Chrome session through a local relay.

Mitigation: Run it only in a dedicated browser profile/session and review browser activity before deployment.

Risk: Product descriptions and scraped Xiaohongshu note data are sent to the configured local LLM pipeline.

Mitigation: Avoid sensitive product information unless the local pipeline is trusted for that data.

Risk: The skill reads a user-provided local product_image path.

Mitigation: Provide only intended image files and avoid sensitive local paths.

Risk: The release includes an obfuscated LLM helper file.

Mitigation: Review or replace wc3-code.mjs before using the skill in a sensitive environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fatmind/skills/xhs-product-trend-fit)

## Skill Output:

**Output Type(s):** [Analysis, Files, JSON, Markdown, HTML]

**Output Format:** [HTML report, JSON summary, Markdown data file, and one-line JSON stdout summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local Chrome relay, an active Xiaohongshu browser session for best results, a local LLM pipeline, Node.js >= 22, and a real local product image path.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

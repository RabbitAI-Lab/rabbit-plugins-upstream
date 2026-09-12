## Description:

Analyzes whether a product has Xiaohongshu promotion fit by using a required product image and description to identify directions, search recent trend evidence, inspect reference posts, and produce an HTML report with heat signals and promotion guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and product teams use this skill before publishing Xiaohongshu product notes to decide whether a product direction has recent heat, what reference posts support it, and how to position the promotion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a logged-in Chrome Xiaohongshu session through a browser relay.

Mitigation: Run it only in a browser session you are comfortable granting to the workflow, and confirm the relay is intended for this task before execution.

Risk: Product descriptions, image paths, scraped note details, and comments are sent into the local LLM pipeline, and WC3_LLM_ENDPOINT can point to a remote service.

Mitigation: Keep WC3_LLM_ENDPOINT local unless the remote provider is trusted with the product and market data.

Risk: The skill reads the supplied local product image and embeds image bytes directly in the generated HTML report.

Mitigation: Use a dedicated product image file and review generated HTML before sharing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fatmind/skills/xhs-product-trend-fit)
- [Publisher profile](https://clawhub.ai/user/fatmind)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [HTML report, JSON summary, Markdown data details, and one-line stdout JSON summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a product image and product description; writes report_path, res.json, and data.md under the configured output directory.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

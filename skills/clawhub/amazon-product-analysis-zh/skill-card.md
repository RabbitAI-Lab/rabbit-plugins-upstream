## Description:

Amazon 商品转视频脚本 turns a single Amazon product link into a Chinese social short-video script grounded in listing claims and public review language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and commerce operators use this skill to analyze one Amazon product page and produce evidence-backed Chinese social-video concepts and shot-by-shot scripts from listing and review text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon browsing can expose regional price displays, login walls, or limited public review samples.

Mitigation: Verify price and market context, avoid account login, and label sample limitations in the generated insights.

Risk: Marketing scripts can overstate product claims if generated copy is not tied to collected evidence.

Mitigation: Keep script lines traceable to listing claims or review language and require human review before publication.

Risk: The current version does not generate final video or perform social-video competitor analysis.

Mitigation: Present the output as planning and scripting material, then route video generation to the user's selected platform.

## Reference(s):

- [Amazon 商品转视频脚本 on ClawHub](https://clawhub.ai/chengyu-xixihaha/skills/amazon-product-analysis-zh)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with product insights, review-language evidence, strategy options, and a shot-by-shot script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may create local markdown deliverables such as insights.md and script.md when used as written.]

## Skill Version(s):

1.0.0 (source: config.yaml and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

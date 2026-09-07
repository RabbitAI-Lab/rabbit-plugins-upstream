## Description:

Helps cross-border sellers and content teams generate Grok-oriented ecommerce sales videos through LinkPix/qhkit, including product-image videos, social media ads, short-form scripts, task polling, and result delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketing teams, and content operators use this skill to prepare ecommerce product videos for platforms such as TikTok, Instagram Reels, Douyin, Xiaohongshu, Amazon, and Shopee. It guides model selection, media upload, credit estimation, generation, status polling, and delivery through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party qhkit/青虎AI CLI for paid video generation and media upload.

Mitigation: Install only when that provider is approved for the intended content, and review what media will be uploaded before generation.

Risk: The security summary notes that API-key handling needs review before installation.

Mitigation: Do not paste API keys into chat; configure tokens through a local secret mechanism or environment variable.

Risk: Generation commands may consume paid credits.

Mitigation: Run the estimate flow where available and confirm the expected credit charge before approving any generate command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-grok-sales)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit commands, model-option guidance, credit-estimate guidance, task IDs, and generated media URLs.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

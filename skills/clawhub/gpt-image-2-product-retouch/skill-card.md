## Description:

Helps agents retouch product photography with GPT Image 2 through AI Hive while preserving product structure, labels, colors, materials, and other sales-relevant facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce operators, and creative teams use this skill to guide AI Hive product-photo retouching workflows, including blemish cleanup, reflection control, edge repair, material and color calibration, package cleanup, and batch SKU consistency. The skill emphasizes preserving factual product details and reviewing each retouched output against the original image before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts are uploaded to AI Hive or a configured base URL.

Mitigation: Use the skill only with images that may be sent to that service, and configure the base URL intentionally.

Risk: Stored API keys may expose AI Hive account access if mishandled.

Mitigation: Prefer environment variables where practical, keep the local config file protected, and avoid sharing configs or logs that contain credentials.

Risk: Retouched images can misrepresent products when defects, second-hand condition, food appearance, or medical product state are material facts.

Mitigation: Compare outputs against originals and preserve factual labels, structure, colors, materials, usage marks, and condition details before publishing.

Risk: Free-form backend parameters can change generation behavior unexpectedly.

Mitigation: Use custom parameters only when their backend effect is understood, then review the generated image before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-product-retouch)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit selected product images and prompts to AI Hive, poll task status, and save generated image files to a configured output directory.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

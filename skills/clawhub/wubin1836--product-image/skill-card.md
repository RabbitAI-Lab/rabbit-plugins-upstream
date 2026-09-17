## Description:

产品图生成 helps agents build a commercial product-image shot matrix and generate catalog, hero, macro, scale-context, and packaging images through AI Hive using Nano Banana 2 while preserving product physical details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, brand teams, merchants, and developers use this skill to plan and run product-image generation workflows for ecommerce listings, website hero imagery, material detail shots, scale scenes, and packaging compositions. It emphasizes reference-based checks so synthetic product images are reviewed against approved product facts before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if passed on the command line or stored with weak local file permissions.

Mitigation: Prefer environment or local config storage, avoid command-line secrets, and keep the local AI Hive config file restricted to the current user.

Risk: Dependency drift in the unpinned requests package can affect reproducibility or supply-chain posture.

Mitigation: Install dependencies in a virtual environment and pin or verify requests when reproducible commercial use matters.

Risk: Reference images and product data are uploaded to AI Hive for generation.

Mitigation: Upload only product or reference images that the user is comfortable sending to AI Hive.

Risk: Generated product imagery can imply incorrect physical details, included accessories, specifications, or performance claims.

Mitigation: Have the brand or merchant compare outputs against approved product references and remove unverified features, accessories, text, or claims before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples, JSON task status, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are downloaded to the configured output directory; task queries can return JSON status and result metadata.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

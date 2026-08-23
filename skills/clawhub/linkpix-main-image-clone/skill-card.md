## Description:

Uses LinkPix and qhkit to analyze a high-performing ecommerce reference image's layout and visual style, then generate a similar 1:1 main image for the user's own product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketers, and agents use this skill to recreate the composition and visual style of a reference product main image while substituting the user's own product images. It guides qhkit setup, cost estimation, user confirmation, generation, and delivery of generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node/npm tooling and qhkit on the local machine.

Mitigation: Use a disposable or managed environment where qhkit is already installed, or review and approve installation commands before allowing the agent to run them.

Risk: The skill handles qhkit credentials and may ask for API keys.

Mitigation: Provide credentials only when the qhkit service is trusted, prefer environment variables or managed secret storage, and avoid exposing tokens in logs or chat history.

Risk: Image generation consumes qhkit credits and submitted generation jobs may not be cancelable.

Mitigation: Run the estimate command first, present the exact parameters and expected credits to the user, and wait for explicit approval before generation.

Risk: Generated ecommerce images may differ from the source product or accidentally retain unwanted text, logos, branding, or reference-image elements.

Mitigation: Ask the user to review key details after generation, use removeText or explicit hints where needed, and avoid directly copying third-party products, brands, logos, or watermarks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and qhkit credit usage after user-approved generation.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

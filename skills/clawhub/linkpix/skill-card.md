## Description:

LinkPix helps agents route ecommerce media requests to Qinghu qhkit workflows for product images, batch image editing, AI video generation, video translation and editing, storyboard creation, advertising assets, POD materials, and short-video or creator data analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and their agents use this skill to select Qinghu qhkit commands for creating product images, listings, advertising videos, translated media, edited videos, storyboards, POD artwork, and campaign analysis outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update qhkit/npm tooling globally.

Mitigation: Run it in a restricted environment and review tooling changes before use.

Risk: The skill can handle a Qinghu API key.

Mitigation: Avoid sharing secrets in ordinary chat when possible and prefer restricted configuration channels or environment variables.

Risk: Some flows upload local media to Qinghu, including workflow estimates.

Mitigation: Review selected files and confirm uploads or paid generation requests before execution.

Risk: Face-replacement and watermark-removal features can be misused.

Mitigation: Use those features only when the user has clear rights and consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media URLs, prompt or script text, task status JSON, credit estimates, and concise user-facing summaries.]

## Skill Version(s):

0.1.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

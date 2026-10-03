## Description:

This skill helps ecommerce operators, short-video teams, and ad buyers use Qinghu AI/LinkPix through qhkit to generate MiniMax H3 product promotion videos from product images and selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce, social video, and advertising teams use this skill to prepare product-video generation requests, choose current LinkPix/qhkit model options, estimate credits, submit jobs, poll status, and return finished video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may request a Qinghu API key and use it to access paid LinkPix/qhkit services.

Mitigation: Use a protected environment variable or secret manager for the token, avoid pasting secrets into chat, and confirm credit estimates before submitting paid generation jobs.

Risk: The skill can configure qhkit locally, install Node/npm packages, and change the local PATH.

Mitigation: Review package installation commands and PATH changes before execution, and prefer an isolated environment when testing the skill.

Risk: Product images or media may be uploaded to Qinghu/LinkPix services during generation.

Mitigation: Use only media that is approved for upload to third-party services and confirm the referenced files before submitting a generation job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-minimax-h3-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated video URLs, task IDs, credit estimates, and status updates from qhkit/LinkPix workflows.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

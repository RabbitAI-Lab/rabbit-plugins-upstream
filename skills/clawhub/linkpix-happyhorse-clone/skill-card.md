## Description:

Helps short-video creators and ecommerce teams analyze reference videos, rewrite scripts around their own products, and guide qhkit commands that generate HappyHorse 1.1-style video assets through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agents use this skill to transform a short-video link into an analyzed script, adapt that structure for a user's product, and prepare user-confirmed qhkit video generation commands for ad or social commerce assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit and related dependencies locally, including mutable global npm installs.

Mitigation: Use a pinned, isolated qhkit installation where possible and review package installation commands before execution.

Risk: The workflow requires a Qinghu API key and may upload selected media to Qinghu services.

Mitigation: Configure credentials through a protected secret mechanism and confirm which local files or URLs will be uploaded before running generation commands.

Risk: Video generation can spend account credits and submitted generation tasks may not be cancellable.

Mitigation: Run estimates when supported, present model, duration, assets, and expected credit cost, and wait for explicit user approval before submitting generate commands.

Risk: Reference-video workflows can encourage copying source material too closely.

Mitigation: Use the reference only for structure and pacing, rewrite scripts around the user's own product and claims, and avoid copying original footage or wording.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-happyhorse-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include rewritten video scripts, qhkit command parameters, polling/status guidance, and generated media URLs after user-confirmed submission.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

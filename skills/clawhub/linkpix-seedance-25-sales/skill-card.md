## Description:

Helps ecommerce and brand teams use qhkit to create Seedance 2.5 product promotion videos from product images, prompts, and selected video parameters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand teams, and creative staff use this skill to configure qhkit video generation for product videos, advertising clips, and social commerce assets. The skill guides model discovery, parameter selection, cost estimation, task submission, polling, and video delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node/npm tooling and qhkit in the local environment.

Mitigation: Review and explicitly approve package installation or upgrade commands before running them, and prefer an isolated environment for execution.

Risk: The skill handles a Qinghu API token for qhkit configuration.

Mitigation: Configure the token through a secure secret mechanism when possible and avoid pasting long-lived credentials into shared logs or transcripts.

Risk: Product images, video references, or audio references may be uploaded to the provider.

Mitigation: Use only media that is approved for external processing and remove confidential or regulated content before submission.

Risk: Video generation can spend provider credits after task submission.

Mitigation: Run estimates when supported and require explicit user confirmation of model, duration, assets, and expected credits before generating.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-seedance-25-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit command plans, cost estimates, task IDs, status updates, and final video URLs.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

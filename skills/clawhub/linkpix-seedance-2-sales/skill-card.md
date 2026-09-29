## Description:

Helps e-commerce operators, ad creative teams, and livestream teams use Qinghu AI qhkit commands to generate Seedance 2.0 product showcase and sales videos from product images, prompts, and selected model options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External teams and developers use this skill to configure qhkit, choose live Seedance 2.0 video model options, estimate credits, submit approved product media, poll task status, and deliver finished e-commerce short-video assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade npm command-line tooling, including unpinned latest-version installs.

Mitigation: Review the qhkit package and requested install or upgrade command before execution; use an approved package source and pinned version when required by policy.

Risk: The workflow uploads selected product images, videos, or audio to the qhkit service.

Mitigation: Use only approved media assets and avoid uploading confidential, personal, or rights-restricted material unless the user has confirmed it is permitted.

Risk: The workflow requires a qhkit API key and may configure it locally.

Mitigation: Prefer a secret store or environment variable, avoid exposing the key in logs or chat, and let the user configure credentials directly when possible.

Risk: Video generation consumes credits and submitted tasks cannot be cancelled.

Mitigation: Run estimates when supported and require explicit user confirmation of model, duration, orientation, reference media, and expected credits before any generate command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-seedance-2-sales)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)
- [Qinghu API Key Guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces task setup, status polling instructions, credit-estimate guidance, and final video URL delivery guidance.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

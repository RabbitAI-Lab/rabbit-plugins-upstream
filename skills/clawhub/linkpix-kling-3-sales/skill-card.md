## Description:

Helps ecommerce and brand content teams generate Kling 3.0 product marketing videos through Qinghu AI and qhkit using product images, prompts, model lookup, task polling, and result download.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, short-video teams, and brand content teams use this skill to prepare and run qhkit video or video-quick workflows for product videos, ads, shopping clips, and social commerce assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to install or upgrade qhkit globally, including @latest upgrades.

Mitigation: Prefer a pinned, preinstalled qhkit runtime and review install commands before execution.

Risk: The skill handles product media and may upload it through qhkit during generation workflows.

Mitigation: Use only media approved for upload to the configured service and avoid sensitive or unreleased assets unless the user has confirmed authorization.

Risk: The skill requires an API token and includes token setup guidance.

Mitigation: Configure the token through a trusted local secret mechanism or environment variable, and do not paste real API keys into chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-kling-3-sales)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit setup, model-selection, estimate, generate, status, and delivery guidance; generated media is produced by the external qhkit service.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

This skill helps Amazon sellers and cross-border ecommerce teams use Qinghu AI through qhkit to generate Amazon product visuals, including white-background main images, carousel images, A+ detail images, comparison images, selling-point graphics, multilingual images, and promotional posters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, Amazon sellers, designers, and cross-border trade teams use this skill to plan and run qhkit image-generation workflows for Amazon main images, carousel sets, detail pages, A+ graphics, multilingual product visuals, and campaign posters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to install or upgrade executable tools.

Mitigation: Review the qhkit package and exact install or upgrade command before execution, pin versions where practical, and run the workflow in a contained environment.

Risk: The skill may request a Qinghu API token through chat.

Mitigation: Configure credentials outside the chat when possible, prefer environment variables or local secret storage, and avoid sharing tokens in conversation transcripts.

Risk: The external image workflow may access local input images and produce generated image URLs.

Mitigation: Limit the agent's file access to the intended product assets and review generated outputs before use in marketplace listings or advertising.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-amazon-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys page](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with inline bash and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit task parameters, estimates, status guidance, and generated image URLs when the external qhkit workflow is executed.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

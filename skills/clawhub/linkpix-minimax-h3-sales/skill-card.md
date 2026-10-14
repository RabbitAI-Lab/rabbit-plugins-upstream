## Description:

Helps ecommerce teams create short product-promotion videos with synchronized speech and visuals through the qhkit video service, using MiniMax H3 when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators, short-video teams, and advertisers use this skill to plan and generate product showcase and promotional videos from product images and selling points. It guides model selection, cost confirmation, generation, and delivery through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating the third-party qhkit package exposes the environment to package supply-chain changes.

Mitigation: Use a vetted local installation or pin the package version when possible.

Risk: Product images, other media, and prompts are sent to the qhkit service.

Mitigation: Only submit materials approved for upload to the external service.

Risk: The service requires an API token, and setup guidance can change the shell environment.

Mitigation: Protect the token and avoid persistent PATH changes unless intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-minimax-h3-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [autoagc publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Video links]

**Output Format:** [Markdown guidance with qhkit commands and links to completed videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires explicit user approval after a cost estimate; results depend on the available models and the external service.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

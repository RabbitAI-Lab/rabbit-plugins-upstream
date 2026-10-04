## Description:

Generates e-commerce marketing assets such as product images, scene images, detail pages, promotional posters, advertising images, and short advertising videos through the LinkPix qhkit workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing operators use this skill to plan and generate bundled e-commerce campaign assets for product promotion, ad placement, event marketing, and brand marketing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit and other host tooling during use.

Mitigation: Use a preinstalled and pinned qhkit version where possible, and review any install or upgrade command before execution.

Risk: The skill sends product media and prompts to the provider through qhkit.

Mitigation: Use the skill only with media that is approved for the provider workflow, and avoid submitting sensitive product or customer data unless permitted.

Risk: The artifact instructs agents to follow upgrade commands returned by an external CLI response.

Mitigation: Do not execute upgrade commands copied from tool output without explicit human review.

Risk: The skill requires an API token for qhkit access.

Mitigation: Store tokens in a secure secret manager or environment variable and avoid embedding credentials in command history or files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-marketing-assets)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with qhkit command examples, JSON CLI parameters, generated media URLs, task IDs, status updates, and credit usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include image and video URLs returned by the provider CLI; video generation may require polling before final delivery.]

## Skill Version(s):

0.1.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Generates ecommerce sales copy and video scripts from product selling points, and can derive scripts from reference viral video links for spoken sales pitches, product seeding, reviews, and plot-based styles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to generate complete ecommerce sales scripts from product images, selling points, and target style guidance. It also supports competitive inspiration workflows by submitting a reference video link and retrieving the resulting video script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The qhkit integration may use a Qinghu/OpenClaw token and upload product images, descriptions, or reference links to the Qinghu/LinkPix service.

Mitigation: Use the skill only with inputs and credentials the user is willing to send to that service, and keep token setup explicit and scoped to the intended environment.

Risk: The skill can install or upgrade the global npm package @iqinghu/qhkit when the command is missing or outdated.

Mitigation: Review global npm/Node installation behavior on the target machine and use npx or a permission-appropriate install path when a global install is unsuitable.

Risk: Script generation and video-inspiration submission create tasks and may consume service credits.

Mitigation: Before any task-submitting command, restate the key parameters and wait for explicit user confirmation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-sales-script)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown response containing complete script text, qhkit command guidance, and configuration notes when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require local product images, product descriptions, reference video URLs, and a Qinghu/OpenClaw token; task-submitting commands require explicit user confirmation.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Generates Chinese e-commerce sales copy and video scripts from product selling points or competitor short-video inspiration links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce content teams use this skill to generate complete product sales scripts, spoken-word copy, seeded-marketing copy, review scripts, and short-video script drafts through the LinkPix qhkit CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade an unpinned global qhkit CLI.

Mitigation: Review install and upgrade commands before execution, and prefer a pinned local qhkit version where possible.

Risk: The skill requires a qhkit API token and may upload product images or videos to an external service.

Mitigation: Avoid exposing the token to unrelated commands, and only provide product media that is acceptable to upload to the external service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-sales-script)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with generated script text and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to return the full generated script text in the response.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

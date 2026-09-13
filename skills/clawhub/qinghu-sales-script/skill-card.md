## Description:

Generates Chinese e-commerce sales scripts, spoken sales copy, product recommendation copy, review scripts, and inspiration scripts from product details or competitor short-video links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to generate e-commerce sales scripts and related short-video copy through Qinghu/qhkit workflows. It supports product-led script generation and competitor-video-inspired script extraction for sales, product seeding, review, and story-style marketing content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade executable Node tools, download Node binaries, and change PATH or shell-profile configuration.

Mitigation: Require user confirmation before npm install, npx execution, Node download, PATH or shell-profile changes, or qhkit upgrades; prefer pinned, isolated installations.

Risk: The skill may upload task inputs, including local media paths supplied for product images or video inspiration, to Qinghu/qhkit services.

Mitigation: Confirm that the user is comfortable sending those inputs to Qinghu/qhkit before running the CLI, and avoid sending sensitive or private materials.

Risk: The skill requires managing a qhkit API token.

Mitigation: Use environment variables or qhkit's token configuration only with user-provided credentials, keep tokens out of transcripts and files, and show only masked configuration during checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-sales-script)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown response with complete generated script text and inline shell commands or CLI JSON when setup and calls are needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill expects qhkit command results as one-line JSON and instructs the agent to deliver the complete script text rather than a summary or link.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

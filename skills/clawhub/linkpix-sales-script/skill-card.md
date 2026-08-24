## Description:

Generates ecommerce sales copy and video scripts from product selling points or reference viral-video links, with support for spoken, seeding, review, and story styles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to generate full LinkPix ecommerce sales scripts or reverse-engineer script drafts from reference short-video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask the agent to install or upgrade qhkit and modify the local environment.

Mitigation: Review install commands and package sources before execution, and run the skill in a controlled environment when possible.

Risk: The skill may upload selected product media or reference links and spend qhkit service credits after confirmation.

Mitigation: Confirm the submitted product media, reference links, language, and account impact with the user before starting credit-consuming tasks.

Risk: The security review notes that the skill asks the agent to collect or store an API key through chat.

Mitigation: Do not paste API keys into chat; configure credentials through a trusted secret, account, or environment mechanism instead.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-sales-script)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu service homepage](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with generated script text and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require qhkit service credentials, media uploads, and user confirmation before credit-consuming task submission.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

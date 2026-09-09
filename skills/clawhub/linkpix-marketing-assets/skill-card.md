## Description:

LinkPix helps agents route e-commerce marketing requests to qhkit workflows that generate product images, scene images, detail pages, promotional posters, ad images, and ad videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to plan and generate e-commerce marketing asset packages for product promotion, paid advertising, seasonal campaigns, and brand marketing. It is intended for requests that span multiple image and video asset types.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install and update an unpinned external npm CLI.

Mitigation: Review the package before installation, prefer a pinned and approved qhkit version, and use the skill only where external npm CLI installation is acceptable.

Risk: The skill relies on a token for qhkit configuration.

Mitigation: Provide credentials through managed secrets or the QHKIT_TOKEN environment variable instead of typing tokens into shell commands.

Risk: The skill can surface upgrade instructions from tool output.

Mitigation: Review upgrade commands before execution and avoid blindly running commands copied from remote or CLI output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-marketing-assets)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides qhkit image and video generation, estimation, polling, and delivery of generated media URLs with charged credits.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

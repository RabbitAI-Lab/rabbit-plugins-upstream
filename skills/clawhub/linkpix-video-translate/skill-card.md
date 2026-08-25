## Description:

The LinkPix video translation skill guides an agent to translate videos into supported languages with AI dubbing, subtitles, and lip-sync package options using qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, localization teams, and developers use this skill to have an agent prepare video translation jobs, configure language and package choices, submit qhkit tasks after confirmation, monitor task status, and return localized video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads user videos to iqinghu.com or autoagc.com and may consume account credits.

Mitigation: Confirm the destination service, job parameters, and expected or actual credit usage before any paid generate action.

Risk: The skill can prompt persistent qhkit, Node, or global package installation and upgrades.

Mitigation: Ask for confirmation before installs or upgrades, and use local or npx execution when global installation is blocked.

Risk: API key handling can expose credentials if users paste tokens into chat.

Mitigation: Have users configure tokens locally or through QHKIT_TOKEN where possible, and avoid echoing or storing API keys in conversation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-translate)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu service](https://www.iqinghu.com)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, status polling guidance, result URLs, local file paths, and credit estimates or actual credit usage when available.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

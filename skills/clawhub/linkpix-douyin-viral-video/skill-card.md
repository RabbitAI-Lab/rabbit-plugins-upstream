## Description:

Helps Douyin commerce operators, live-stream teams, and short-video creators use LinkPix/qhkit workflows to generate vertical product videos, storyboard scripts, task estimates, status checks, and delivery URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce teams, and their agents use this skill to prepare Douyin-oriented product video requests, select available qhkit video models, estimate credits, submit generation tasks after confirmation, poll task status, and return generated video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to install or upgrade mutable third-party tools such as qhkit.

Mitigation: Use a preinstalled or pinned qhkit version where possible and review package updates before automatic installation or upgrade.

Risk: The workflow may require API keys and account credits for LinkPix/qhkit video generation.

Mitigation: Configure credentials outside chat when possible, use narrowly scoped keys with spending limits, and confirm credit estimates before generation.

Risk: Uploaded product images or media may be handled by qhkit/LinkPix during generation.

Mitigation: Install only when that media handling is acceptable and avoid uploading sensitive or restricted media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-douyin-viral-video)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, credit estimates, status summaries, and generated video URLs returned by the CLI.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

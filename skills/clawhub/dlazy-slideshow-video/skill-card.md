## Description:

Turns slides or documents into narrated slideshow videos with voiceover and transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can turn slides or documents into narrated explainer, report, courseware, or training videos, and continue work in a project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages and attached documents are sent to dLazy, and attached files are uploaded to its media storage; retention practices are not verified.

Mitigation: Only attach documents you are comfortable sharing with dLazy, and check that you are using the intended project.

Risk: Using the hosted service may consume organization credits, and the CLI saves an API key in its local configuration.

Mitigation: Consider service credit costs before generating videos, protect the local CLI configuration, and rotate or revoke the key if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, Text, Shell commands]

**Output Format:** [Narrated slideshow video and text responses; usage instructions in Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation runs through the dLazy service; attached files are uploaded for processing.]

## Skill Version(s):

1.0.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

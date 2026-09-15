## Description:

Turns slides, photos, or documents into narrated slideshow-style videos with voiceover and transitions through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to ask dLazy's hosted file-to-video agent to convert documents, slides, and reference files into explainer, training, report, or courseware slideshow videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached local documents are uploaded to dLazy API and file storage during normal use.

Mitigation: Avoid attaching sensitive documents unless the user's organization permits sharing them with dLazy's hosted service.

Risk: A dLazy API key is required and may be stored in the local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local CLI configuration, avoid exposing the key in logs, and rotate or revoke the key if the environment or package is suspected to be compromised.

Risk: Global installation persists the @dlazy/cli binary on the system.

Mitigation: Prefer the pinned npx invocation when a persistent global binary is not desired, and install only if the dLazy CLI package is trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands; dLazy CLI responses may include project status, URLs, and generated video artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a pinned @dlazy/cli install path and a project-scoped hosted file-to-video agent.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

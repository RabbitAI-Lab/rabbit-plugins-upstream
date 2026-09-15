## Description:

Operates Label Studio through an OOMOL-connected account to read user, project, and task data and create projects or tasks through the Label Studio connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations users use this skill to inspect Label Studio account context, projects, and tasks, then create projects or individual tasks when the requested payload is clear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include direct execution of remote installer scripts.

Mitigation: Review the setup path before installation, prefer a verified or package-manager-based oo CLI install, and do not run remote installer commands from an elevated shell unless independently verified.

Risk: Write actions can create Label Studio projects or tasks.

Mitigation: Approve write actions only after the exact project or task payload and expected effect are clear.

## Reference(s):

- [Label Studio homepage](https://labelstud.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-label-studio)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Skill icon](https://static.oomol.com/logo/third-party/label_studio.svg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector action names, schema inspection commands, JSON payloads, and safety confirmations for write actions.]

## Skill Version(s):

1.0.2 (source: metadata.version and release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

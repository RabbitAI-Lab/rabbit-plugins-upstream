## Description:

Turns document-based requests into explainer, report, or training video projects through dLazy's hosted agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users can use this skill to turn a document into an explainer, report, courseware, or training video by directing the dLazy file-to-video agent and continuing work in a project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to dLazy services, attached files are uploaded to its media storage, and the security review noted login and project-listing commands whose purpose was unclear.

Mitigation: Review prompts and attachments before sending them, and confirm that the CLI commands and project access are expected for your use.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository link listed in the skill documentation](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Video project artifacts, Shell commands, Configuration guidance]

**Output Format:** [Text responses and video project artifacts generated through the dLazy service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped, multi-turn workflow; attached files are uploaded to dLazy media storage.]

## Skill Version(s):

1.0.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

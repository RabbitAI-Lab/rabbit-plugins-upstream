## Description:

LangSmith lets agents inspect schemas and run LangSmith actions for datasets, examples, projects, and workspaces through the OOMOL `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to work with LangSmith datasets, examples, projects, and workspaces from an OOMOL-connected account. It supports reading LangSmith resources and creating datasets, examples, or tracing projects after confirming state-changing payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include internet installer commands that can execute code on the user's machine.

Mitigation: Review the installer source independently and use the documented installer only when the source and publisher are trusted.

Risk: Write actions can create or modify LangSmith datasets, examples, and tracing projects.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running state-changing actions.

Risk: LangSmith action payloads can include sensitive dataset inputs, outputs, or metadata.

Mitigation: Avoid sending secrets or sensitive data unless required, and confirm the connected account and scope before executing actions.

## Reference(s):

- [LangSmith homepage](https://www.langchain.com/langsmith)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub LangSmith skill](https://clawhub.ai/oomol/skills/oo-langsmith)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing LangSmith actions require confirmation of the exact payload and effect before execution.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and artifact metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

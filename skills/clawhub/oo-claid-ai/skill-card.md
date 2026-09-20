## Description:

Claid AI (claid.ai). Use this skill for ANY Claid AI request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Claid AI through an OOMOL-connected account, including synchronous image edits and asynchronous image-edit task submission and polling. The skill guides agents to inspect the live connector schema before constructing payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup includes remote installer commands for the oo CLI.

Mitigation: Review the installation method first, prefer an official package manager or verified download path, and do not run the remote installer automatically unless OOMOL and the install URL are trusted.

Risk: Image editing actions can change Claid AI state.

Mitigation: Confirm the exact image-edit payload and expected effect with the user before running write actions.

## Reference(s):

- [Claid AI homepage](https://claid.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Claid AI skill page](https://clawhub.ai/oomol/skills/oo-claid-ai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo connector commands; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.4 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

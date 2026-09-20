## Description:

Zep (getzep.com). Use this skill for ANY Zep request: reading, creating, updating, and deleting data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to operate Zep memory projects through an OOMOL-connected account, including project lookup, user and thread management, message ingestion, and context retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation language may cause the skill to be used for Zep-related requests without enough user intent.

Mitigation: Use the skill only for explicit Zep operations requested by the user.

Risk: The skill documents first-time installer commands that pipe remote scripts into a shell.

Mitigation: Avoid those installers unless the OOMOL CLI source has been independently trusted and verified.

Risk: Write and destructive actions can alter or delete Zep users, threads, messages, and memory artifacts.

Mitigation: Require confirmation of the exact target, payload, and expected effect before running write or delete actions.

## Reference(s):

- [Zep homepage](https://www.getzep.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-zep)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include oo CLI command results containing Zep data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

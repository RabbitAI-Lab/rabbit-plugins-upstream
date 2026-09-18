## Description:

Easy8 (easy8.com). Use this skill for Easy8 requests involving reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Easy8 projects and tasks through the oo CLI, including listing, retrieval, creation, updates, and deletion with schema-aware payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents remote installer commands that execute mutable shell scripts.

Mitigation: Install the oo CLI only through a trusted, verified method and do not allow an agent to run installer commands automatically.

Risk: Easy8 write and destructive actions can modify or permanently delete tasks and projects.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or delete actions.

## Reference(s):

- [Easy8 homepage](https://www.easy8.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Easy8 skill page](https://clawhub.ai/oomol/skills/oo-easy8)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

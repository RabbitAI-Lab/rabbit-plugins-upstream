## Description:

Mem0 (mem0.ai). Use this skill for ANY Mem0 request - reading, creating, updating, and deleting data. Whenever a task involves Mem0, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Mem0 memories and related account data through an OOMOL-connected account, including search, retrieval, history inspection, creation, updates, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote oo CLI installer commands could execute unverified code.

Mitigation: Review installation steps first; prefer a verified, pinned, or package-manager installation source, and do not let an agent run the remote installer automatically.

Risk: Mem0 write and delete actions can change or remove memory data.

Mitigation: Require explicit user confirmation of the exact payload, target, and expected effect before running write or destructive actions.

## Reference(s):

- [Mem0 homepage](https://mem0.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mem0)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

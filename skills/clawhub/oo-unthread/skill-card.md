## Description:

Use this skill to read, create, update, and delete Unthread account records through OOMOL's connected-account CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when an agent needs to manage external customer accounts in Unthread. It supports account retrieval, listing, creation, updates, and deletion through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, and permanently delete Unthread account records.

Mitigation: Review the exact target, payload, and expected effect before approving write or destructive actions.

Risk: Connector payloads can become invalid if action schemas change.

Mitigation: Inspect the live action schema before constructing or running each connector request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-unthread)
- [Unthread homepage](https://unthread.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect the live connector schema before action execution and require explicit approval for write or destructive actions.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

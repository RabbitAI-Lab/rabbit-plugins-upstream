## Description:

Enables an agent to operate Dart through the OOMOL oo CLI for reading, creating, updating, and deleting Dart task data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Dart tasks and workspace configuration through an OOMOL-connected account. The skill supports read, write, and destructive task actions with explicit confirmation expected for state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review the installer path before use, or prefer a verified package, pinned release, checksum, or manual installer review.

Risk: Connecting Dart gives the skill access to read and modify tasks through the connected account.

Mitigation: Confirm exact payloads and effects before write actions, require explicit approval for destructive actions, and use the least-privileged connected account available.

## Reference(s):

- [Dart homepage](https://www.dartai.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dart)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON data from the OOMOL oo connector when actions are executed.]

## Skill Version(s):

1.0.2 (source: server evidence release.version and frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

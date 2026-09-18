## Description:

Operate GitHub through an OOMOL-connected account for reading, creating, updating, and deleting repository, issue, pull request, release, workflow, branch, commit, label, milestone, and file data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage GitHub resources through the OOMOL-connected oo CLI while relying on live action schemas for request payloads. It supports read, write, and destructive GitHub workflows, including repository, issue, pull request, release, GitHub Actions, and file operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands that could be unsafe if run blindly.

Mitigation: Prefer an official, verifiable installation method and review installer sources before execution.

Risk: The skill can perform write and destructive GitHub operations, including deleting files, releases, labels, refs, comments, collaborators, and repositories.

Mitigation: Confirm the exact target, payload, and expected effect with the user before any write or destructive action runs.

Risk: Using OOMOL as a GitHub connector requires granting permissions appropriate to the requested tasks.

Mitigation: Install only with the GitHub scopes needed for the intended workflow and reconnect credentials when scope or credential errors occur.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-github)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [GitHub](https://github.com)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL GitHub Connection Settings](https://console.oomol.com/app-connections?provider=github)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before execution and returns connector responses as JSON when commands are run.]

## Skill Version(s):

1.0.9 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

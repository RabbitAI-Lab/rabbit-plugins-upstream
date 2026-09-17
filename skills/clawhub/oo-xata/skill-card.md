## Description:

Xata lets agents read Xata organizations, projects, branches, branch details, and available deployment regions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Xata account, project, and branch metadata from an authenticated OOMOL connection without handling raw Xata tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup fallback instructions include remote installer commands that could execute local code if run automatically or without verification.

Mitigation: Review the oo CLI installation path before installing; use a verified, version-pinned, checksum-checked install method and do not let an agent run the remote installer automatically.

Risk: The connector depends on a live OOMOL account, Xata connection scope, credentials, and billing status.

Mitigation: Run read actions only after the CLI is installed and authenticated; resolve scope, credential, app, or billing errors through the documented OOMOL console steps before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-xata)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Xata homepage](https://xata.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

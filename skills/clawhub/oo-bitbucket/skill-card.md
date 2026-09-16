## Description:

Use this skill to read, create, update, and delete Bitbucket data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Bitbucket repositories, pull requests, issues, pipelines, snippets, workspaces, and related resources through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct remote script execution for installing the oo CLI.

Mitigation: Review the installer path before use, prefer a signed or otherwise verifiable release, and do not run setup from an elevated shell.

Risk: The skill can perform high-impact Bitbucket write and delete actions.

Mitigation: Approve write or destructive actions only after checking the exact target and payload.

## Reference(s):

- [ClawHub Bitbucket skill page](https://clawhub.ai/oomol/skills/oo-bitbucket)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Bitbucket](https://bitbucket.org)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs return JSON with data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

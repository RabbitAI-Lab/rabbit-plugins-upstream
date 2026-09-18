## Description:

Torii (toriihq.com). Use this skill for ANY Torii request - searching and reading data. Whenever a task involves Torii, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to search and read Torii organization data through an OOMOL-connected oo CLI account, including apps, contracts, users, transactions, workflows, and organization details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes running a remote installer directly in a shell.

Mitigation: Review official installation guidance, use a pinned or verified artifact when available, and avoid running remote installers blindly.

Risk: The connector can access broad Torii organization data.

Mitigation: Install only if OOMOL is trusted for the workspace, confirm account connection scope, and avoid retrieving broad organization data unless it is needed for the user request.

## Reference(s):

- [Torii Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-torii)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Installation Guide](https://cli.oomol.com/install-guide.md)
- [Torii Homepage](https://www.toriihq.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live action schema before constructing a connector payload.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

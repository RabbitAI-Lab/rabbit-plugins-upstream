## Description:

Laravel Cloud (cloud.laravel.com). Use this skill for ANY Laravel Cloud request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Laravel Cloud organizations, applications, environments, deployments, and available regions through an OOMOL-connected Laravel Cloud account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can run a remote oo CLI installer directly in a shell without verification.

Mitigation: Review OOMOL's official install instructions first, download installers without immediate execution, and verify signatures or checksums before running them.

Risk: Connector calls depend on OOMOL as an intermediary for Laravel Cloud account access.

Mitigation: Install only when that intermediary model is acceptable for the deployment, and keep Laravel Cloud credentials managed through the connected account.

## Reference(s):

- [Laravel Cloud Skill Page](https://clawhub.ai/oomol/skills/oo-laravel-cloud)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Laravel Cloud](https://cloud.laravel.com)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

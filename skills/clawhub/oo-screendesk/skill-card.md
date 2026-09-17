## Description:

Use this skill for Screendesk requests that read, create, or update Screendesk data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and workspace administrators use this skill to list, retrieve, search, and update Screendesk recordings and related workspace user information through an authenticated OOMOL-connected Screendesk account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that can execute network-delivered code, and the security summary flags this release as suspicious for that reason.

Mitigation: Review the setup path before installation; prefer a verified, version-pinned, or package-manager installation flow, and do not run remote installer pipelines unless OOMOL's distribution channel is trusted.

Risk: The skill can update Screendesk recording titles, summaries, and descriptions.

Mitigation: Confirm the exact update payload and expected effect with the user before running the write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-screendesk)
- [Screendesk Homepage](https://screendesk.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may return connector JSON responses containing Screendesk data and an OOMOL execution identifier.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Adyen (adyen.com). Use this skill for ANY Adyen request - searching and reading data. Whenever a task involves Adyen, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Adyen connector schemas and retrieve Adyen company, merchant, and API credential details through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer commands include direct pipe-to-shell patterns.

Mitigation: Review installation steps before running them and prefer official, verifiable installer documentation.

Risk: The get_api_credential action can return credential metadata and account information may be sensitive.

Mitigation: Use a narrowly scoped Adyen connection, invoke credential-detail actions only when needed, and handle returned account data as sensitive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-adyen)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [Adyen Homepage](https://www.adyen.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schema and run commands; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

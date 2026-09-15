## Description:

TinyURL helps an agent create short links and list account URLs through the OOMOL-connected TinyURL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate TinyURL through an OOMOL-connected account, including creating short URLs and listing existing URLs by availability status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Review the installer path first, prefer a verified package manager or pinned signed release, and avoid direct curl|bash or irm|iex execution unless the OOMOL delivery chain is trusted.

Risk: The create_short_url action changes TinyURL account state by creating a new short link.

Mitigation: Confirm the exact destination URL and JSON payload with the user before running the write action.

## Reference(s):

- [ClawHub TinyURL Skill](https://clawhub.ai/oomol/skills/oo-tinyurl)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [TinyURL Homepage](https://tinyurl.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, JSON payloads]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector JSON responses when commands run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

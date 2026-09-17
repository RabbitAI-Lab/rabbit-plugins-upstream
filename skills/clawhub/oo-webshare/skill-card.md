## Description:

Webshare (webshare.io) skill for searching and reading account, proxy configuration, proxy list, and usage data through an OOMOL-connected Webshare connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Webshare account profile, proxy configuration, proxy lists, and hourly proxy usage statistics through the OOMOL oo CLI without handling raw Webshare API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes remote installer commands that run with local shell privileges.

Mitigation: Review the oo CLI installation path before installing, and prefer a pinned, signed, or checksum-verified installer from trusted documentation.

Risk: Read actions can expose Webshare account profile, proxy configuration, proxy lists, and hourly usage statistics through the connected OOMOL account.

Mitigation: Run only the requested read action and avoid exposing returned account or proxy details beyond the user's stated need.

Risk: Connector action schemas may change over time.

Mitigation: Inspect the live action schema with oo connector schema before constructing each action payload.

## Reference(s):

- [Webshare Homepage](https://www.webshare.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

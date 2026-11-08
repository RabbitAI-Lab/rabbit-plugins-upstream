## Description:

Search GIF providers with CLI/TUI, download results, and extract stills/sheets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can search Tenor and Giphy, review results in a terminal interface, and download GIFs or extract still images and frame sheets for documentation and sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial because two skill references could not be resolved.

Mitigation: Review the unresolved references before installing, as recommended by the security assessment.

Risk: GIPHY API access uses a credential, and GIFs are downloaded from external providers.

Mitigation: Keep API keys private; verify downloaded GIF type and animation, and record the asset's attribution, license, and source before using it.

## Reference(s):

- [Gifgrep homepage](https://gifgrep.com)
- [Gifgrep on ClawHub](https://clawhub.ai/hillstreet-ph/skills/gifgrep)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI commands, JSON results or selected fields, downloaded GIFs, and PNG stills or frame sheets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results can be piped or filtered; downloads are saved to ~/Downloads by default, and stills or sheets can be written to a specified path.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

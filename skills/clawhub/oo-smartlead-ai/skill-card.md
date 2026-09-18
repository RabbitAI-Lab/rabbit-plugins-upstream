## Description:

Smartlead helps agents retrieve campaign, lead, and email-account data through an OOMOL-connected Smartlead account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to inspect Smartlead campaigns, campaign leads, and email accounts through connected OOMOL credentials without handling raw Smartlead tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes unverified remote pipe-to-shell commands for installing the oo CLI.

Mitigation: Review the installation path before use and prefer a pinned, signed, or checksum-verified oo CLI release or documented package-manager installation.

Risk: Use beyond the disclosed read-only Smartlead actions could change the risk profile.

Mitigation: Limit intended use to the listed get and list actions unless a future version clearly discloses and scopes write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-smartlead-ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Smartlead Homepage](https://www.smartlead.ai)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing JSON payloads and runs disclosed Smartlead get/list actions through the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

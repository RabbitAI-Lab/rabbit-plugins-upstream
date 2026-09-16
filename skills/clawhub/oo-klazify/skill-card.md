## Description:

Klazify routes Klazify website categorization and domain-enrichment requests through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Klazify action schemas and run read-only website categorization, company profile, domain expiration, logo, IAB category, similar-domain, social-link, and technology-stack lookups through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include internet-downloaded installers executed directly in a shell.

Mitigation: Install only from a trusted OOMOL CLI distribution path, and prefer a verified or package-manager install when available.

Risk: Website and domain lookups may send confidential internal URLs to OOMOL or Klazify.

Mitigation: Submit internal or confidential URLs only when authorized to share them with OOMOL and Klazify.

## Reference(s):

- [ClawHub Klazify Skill](https://clawhub.ai/oomol/skills/oo-klazify)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Klazify Homepage](https://www.klazify.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before requests; OOMOL injects credentials server-side.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

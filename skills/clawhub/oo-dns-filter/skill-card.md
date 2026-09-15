## Description:

DNSFilter (dnsfilter.com). Use this skill for ANY DNSFilter request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query DNSFilter account data through an OOMOL-connected account, including networks, policies, categories, applications, IP address records, the current user, and the public IP observed by DNSFilter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that execute downloaded scripts.

Mitigation: Review the official installation instructions and prefer versioned, integrity-checked CLI installation before using the skill.

Risk: The skill depends on OOMOL as the connector path for DNSFilter access.

Mitigation: Install only when use of OOMOL and the oo CLI is acceptable for the DNSFilter account and operating environment.

## Reference(s):

- [DNSFilter homepage](https://www.dnsfilter.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dns-filter)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions and returns connector responses as JSON when commands are executed.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

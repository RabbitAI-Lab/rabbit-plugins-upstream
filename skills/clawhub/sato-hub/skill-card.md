## Description:

Helps agents research onchain tooling, compare projects, check packages before installation, and cite measured agent-economy figures through Sato Hub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[satohubai](https://clawhub.ai/user/satohubai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Sato Hub to find and compare onchain-agent components, perform pre-installation checks, and report sourced adoption metrics and project details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The referenced Sato Hub tools include remote write actions despite the skill's read-only description; these can store contact, project, wallet, signature, or swap-receipt details.

Mitigation: Review tool permissions before installation and use only lookup or preflight actions unless you intentionally want to submit data to Sato Hub; inspect any details before a write action.

## Reference(s):

- [Sato Hub ClawHub release](https://clawhub.ai/satohubai/skills/sato-hub)
- [Sato Hub MCP documentation](https://satohub.ai/mcp)
- [Sato Hub tool reference](references/tools.md)
- [Sato Hub REST reference](references/rest.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown or JSON query results, with cited links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listing results include source pages; measured figures should retain their date, stage, method, and sample size.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

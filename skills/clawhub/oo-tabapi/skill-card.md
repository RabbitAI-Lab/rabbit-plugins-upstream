## Description:

TabAPI (tabapi.com). Use this skill for ANY TabAPI request — searching and reading data. Whenever a task involves TabAPI, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate TabAPI through an OOMOL-connected account for public URL capture, Markdown extraction, Google Search, and domain intelligence lookups without handling raw TabAPI credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested public URL, domain, search, and lookup payloads are sent to TabAPI through the user's OOMOL-connected account.

Mitigation: Share only URLs, domains, and search terms appropriate for TabAPI processing, and confirm sensitive or account-billed lookups before execution.

Risk: First-time setup may install and authenticate the oo CLI and connect a TabAPI account.

Mitigation: Run setup only after an auth, connection, or missing-command failure, and let the user complete account connection and billing steps intentionally.

Risk: Connector schemas can change over time, making stale payload assumptions unreliable.

Mitigation: Inspect the live action schema with `oo connector schema` before constructing or running each payload.

## Reference(s):

- [TabAPI homepage](https://tabapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tabapi)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Markdown, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or TabAPI JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live connector schemas before action execution; may return hosted PNG URLs, extracted Markdown, search results, DNS/RDAP/WHOIS data, backlink metrics, and traffic estimates.]

## Skill Version(s):

1.0.0 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Lusha helps agents search and read Lusha company, contact, enrichment, and account usage data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to search Lusha companies and contacts, enrich returned records, and check usage, credits, limits, and plan information through a connected OOMOL/Lusha account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes commands that execute remote installer scripts.

Mitigation: Have a human review the installer path and install the oo CLI from a signed, versioned, verifiable source; do not let an agent run curl-to-bash or irm-to-iex setup commands automatically.

Risk: Search and enrichment requests can send company or contact identifiers to OOMOL/Lusha and can return personal contact data under the connected account.

Mitigation: Confirm the user is authorized to process the requested data, limit payloads to necessary identifiers, and handle returned contact data according to the user's approved data policy.

Risk: Lusha operations can depend on account credits, rate limits, and plan settings.

Mitigation: Check usage, credit balance, limits, and billing errors before retrying high-volume searches or enrichment requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lusha)
- [ClawHub publisher profile](https://clawhub.ai/user/oomol)
- [Lusha homepage](https://www.lusha.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include JSON data returned by the Lusha connector.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

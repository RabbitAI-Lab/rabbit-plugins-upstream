## Description:

Autobound (autobound.ai). Use this skill for ANY Autobound request - searching and reading data. Whenever a task involves Autobound, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Autobound through an OOMOL-connected account for company and contact enrichment, signal search, account lookup, signal type listing, and credit-balance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions direct users to pipe remote installer scripts directly into bash or PowerShell.

Mitigation: Prefer an official, versioned oo CLI installation method with checksum or signature verification before using the connector.

Risk: The skill accesses Autobound account data, credit balance, company records, contact records, and signal metadata through an authenticated OOMOL connector.

Mitigation: Use the skill only with an intended OOMOL account and connected Autobound workspace, and inspect the live action schema before submitting payloads.

## Reference(s):

- [Autobound homepage](https://www.autobound.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL Autobound connection settings](https://console.oomol.com/app-connections?provider=autobound)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are requested as JSON and include data plus execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

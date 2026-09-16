## Description:

SearchApi helps agents search and read SearchApi data through the OOMOL-connected search_api connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect SearchApi action schemas, run search requests, retrieve cached results, look up canonical locations, and view account usage through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes one-line remote installer commands for the OOMOL CLI.

Mitigation: Prefer an official signed or package-manager install path when available, verify installer contents where possible, and run setup only after an authentication or missing-command failure.

Risk: SearchApi requests and account usage flow through OOMOL's oo CLI connector.

Mitigation: Install only when comfortable with OOMOL-mediated SearchApi access and connect only the intended SearchApi API key.

## Reference(s):

- [SearchApi homepage](https://www.searchapi.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses server-side credential injection through OOMOL; command output may include SearchApi JSON or HTML result data.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

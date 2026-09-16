## Description:

StoreCensus (storecensus.com). Use this skill for ANY StoreCensus request — searching and reading data. Whenever a task involves StoreCensus, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query StoreCensus ecommerce intelligence, including website details, Shopify app listings, app categories, and filtered ecommerce store search results through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands for the OOMOL CLI, and the security scan flags this as suspicious.

Mitigation: Install the CLI only after independently verifying and trusting the installation source; prefer an already installed, signed-in CLI when available.

Risk: StoreCensus access depends on an OOMOL-connected account with server-side managed credentials, so failed commands may reveal missing, expired, or insufficient connection state.

Mitigation: Follow setup fallback steps only after a command fails with the matching authentication, connection, or billing error.

## Reference(s):

- [StoreCensus homepage](https://www.storecensus.com)
- [StoreCensus skill page on ClawHub](https://clawhub.ai/oomol/skills/oo-storecensus)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are mediated through StoreCensus connector schemas and may include execution metadata from the OOMOL CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

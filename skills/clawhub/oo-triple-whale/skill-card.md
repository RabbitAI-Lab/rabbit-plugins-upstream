## Description:

Helps agents access Triple Whale data through an OOMOL-connected account for schema inspection, analytics queries, attribution exports, summary metrics, and API key validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Triple Whale data workflows through OOMOL, including retrieving live action schemas, running store and date-period analytics requests, exporting customer journey attribution data, and validating connection metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands for the oo CLI without verification.

Mitigation: Use official, versioned installation instructions with signature or checksum verification before running installer commands.

Risk: Triple Whale data access is mediated through OOMOL, including custom SQL queries and analytics exports.

Mitigation: Install only when OOMOL is an acceptable intermediary and review store, date range, and query payloads before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-triple-whale)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Triple Whale Homepage](https://www.triplewhale.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include connector command results and setup guidance when authentication, connection, or billing errors occur.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

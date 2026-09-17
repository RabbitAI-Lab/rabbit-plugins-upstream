## Description:

Massive (Polygon.io) provides agent-driven access to Polygon.io market data through OOMOL's oo CLI connector for searching and reading ticker, exchange, market status, and aggregate bar data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Polygon.io market data through an OOMOL-connected account, including aggregate bars, previous-day bars, market status, ticker details, exchanges, ticker types, and filtered ticker searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup documents remote shell and PowerShell installer commands without integrity checks.

Mitigation: Use a trusted, verified installation process for the oo CLI and do not let agents run the documented installer commands automatically.

Risk: Future connector actions may include write or destructive operations even though the listed Polygon.io actions are read-oriented.

Mitigation: Confirm any action not in the documented get/list action set, including the exact payload and expected effect, before execution.

Risk: Market data lookups can be stale, incomplete, or shaped by account permissions and billing status.

Mitigation: Use returned data as a source-specific lookup result, check execution errors and billing or credential failures, and avoid treating it as independently verified financial advice.

## Reference(s):

- [Massive (Polygon.io) Skill Page](https://clawhub.ai/oomol/skills/oo-polygon-io)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Massive (Polygon.io) Homepage](https://massive.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON request payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns connector responses as JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

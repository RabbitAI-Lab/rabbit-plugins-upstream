## Description:

Triple Whale helps an agent retrieve Triple Whale analytics, customer journey attribution exports, Summary Page metrics, custom SQL query results, and API key metadata through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to query Triple Whale store analytics, export attribution data, retrieve summary metrics, and validate connected API key metadata from an OOMOL-managed Triple Whale connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags broad data-query authority for custom SQL and export actions.

Mitigation: Run custom SQL and export actions only for specific user-approved requests and limit payloads to the requested store and date period.

Risk: The security review flags one-line shell installer commands as unsafe to run without review.

Mitigation: Prefer a verified, pinned, or package-manager-based oo CLI installation method before using the connector.

Risk: Triple Whale analytics and attribution exports may expose sensitive account data.

Mitigation: Confirm the intended action, store, date range, and output destination before retrieving or sharing data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-triple-whale)
- [Triple Whale homepage](https://www.triplewhale.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can cause the agent to run oo CLI commands that return Triple Whale data as JSON.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Clari Copilot connector for searching and reading Clari Copilot data through OOMOL instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Clari Copilot calls, transcripts, summaries, scorecards, topics, and workspace users through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to run internet installer scripts directly in a shell.

Mitigation: Review the installer path first, prefer pinned or signed oo CLI releases, inspect downloaded scripts before execution, and avoid elevated shells.

Risk: Clari Copilot calls may include transcripts, summaries, user lists, and media URLs routed through OOMOL.

Mitigation: Confirm that the organization's data handling policies allow using OOMOL for these Clari Copilot requests before connecting the account.

Risk: Connector payloads may be malformed or target unintended Clari Copilot records if built without the current action contract.

Mitigation: Fetch the live action schema before constructing payloads and confirm any write or destructive action payload with the user before execution.

## Reference(s):

- [Clari Copilot homepage](https://www.clari.com/products/copilot/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clari-copilot)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before execution; first-time setup guidance is used only after authentication, connection, or CLI availability failures.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Provides WebScraping.AI access through an OOMOL-connected oo CLI workflow for extracting text, fetching rendered HTML, selecting page areas, and checking account details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read web page text or HTML through WebScraping.AI, inspect live connector schemas, and run read-oriented scraping or account actions without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may execute unverified remote installer scripts for the oo CLI.

Mitigation: Prefer a verified release or package manager, inspect installer contents first, and avoid elevated shells.

Risk: Connecting WebScraping.AI requires selecting an account and API-key scope.

Mitigation: Confirm the intended account and API-key scope before connecting WebScraping.AI.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-webscraping-ai)
- [WebScraping.AI homepage](https://webscraping.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when commands run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

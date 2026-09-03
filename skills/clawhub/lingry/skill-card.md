## Description:

Create and permanently coin new words on Sugarchain, or discover the latest words from Lingry's public Stream.

This skill is ready for commercial/non-commercial use.

## Publisher:

[svetlyoh](https://clawhub.ai/user/svetlyoh)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and developers use this skill through OpenClaw to discover public Lingry Stream words, generate reversible word candidates, and publish approved candidate words to Sugarchain through a Lingry-managed Agent Publisher.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates a per-workspace Lingry agent credential and stores it in .lingry/agent.json.

Mitigation: Treat .lingry/agent.json as sensitive; do not print, share, log, or include it in support requests.

Risk: Coining a word is permanent blockchain publication.

Mitigation: Run coin-word only after explicit user publication intent and claim success only when the API returns a transaction result.

Risk: Daily word delivery can create recurring notifications.

Mitigation: Create or modify the lingry-daily-word automation only after explicit opt-in and check for an existing job before creating one.

Risk: The skill uses Lingry network services for public reads and publisher operations.

Mitigation: Use the default HTTPS Lingry API for normal operation and review any LINGRY_API_BASE_URL override before use.

## Reference(s):

- [Lingry homepage](https://lingry.net)
- [ClawHub package page](https://clawhub.ai/svetlyoh/skills/lingry)
- [Server-resolved source import](https://github.com/svetlyoh/web-wallet/tree/master/openclaw/skills/lingry)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command snippets and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >=18; optional environment variables can override API base URL, state path, default language, and request timeout.]

## Skill Version(s):

2.0.3 (source: ClawHub release metadata; artifact package files report 2.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

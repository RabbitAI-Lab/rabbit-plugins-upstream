## Description:

Interact with teemtape stock watchlists and anonymous notes via the teemtape CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kiwifellows](https://clawhub.ai/user/kiwifellows)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate teemtape watchlists: creating or sharing watchlists, searching ticker symbols, reading delayed quotes, and reading or posting concise anonymous notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Watchlist tokens, Pro access tokens, and share URLs can expose private watchlist access if logged or shared.

Mitigation: Treat these values as sensitive, avoid echoing them in chat or logs, and use masked configuration output where available.

Risk: Using npx without a pinned package version may resolve a newer CLI than the one reviewed with this release.

Mitigation: In higher-security environments, use a pinned or locally reviewed @teemtape/cli version.

Risk: Stock quotes are delayed and notes are public anonymous comments, so outputs may be unsuitable for trading decisions or private analysis.

Mitigation: Use the data for informational workflows only, read existing notes before posting, and keep posted notes concise and non-sensitive.

## Reference(s):

- [teemtape CLI command reference](references/commands.md)
- [teemtape CLI JSON output shapes](references/json-output.md)
- [teemtape ClawHub skill page](https://clawhub.ai/kiwifellows/skills/teemtape-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Use --json for machine-readable CLI output; tokens, Pro access tokens, and share URLs should be treated as sensitive.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

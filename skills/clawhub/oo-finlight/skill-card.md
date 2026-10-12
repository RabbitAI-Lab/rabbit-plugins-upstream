## Description:

Helps agents search financial news, retrieve articles, and discover news sources in Finlight through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Finlight users can ask an agent to find financial news by ticker, sentiment, source, region, or date, read articles by URL, and identify available news sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions pipe a remote installer directly into a shell.

Mitigation: Check the official installation guide and verify the installer source; do not allow an agent to run the installer automatically.

Risk: Finlight access is mediated by OOMOL.

Mitigation: Use this skill only if you are comfortable using OOMOL as an intermediary for Finlight access.

## Reference(s):

- [Finlight skill on ClawHub](https://clawhub.ai/oomol/skills/oo-finlight)
- [Finlight](https://finlight.me/)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown responses with optional structured article data and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Finlight searches, article lookups, and source lists depend on the user's OOMOL connection.]

## Skill Version(s):

1.0.0 (source: skill metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

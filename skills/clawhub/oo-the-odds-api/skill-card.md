## Description:

The Odds API skill helps agents search and read live odds, events, scores, participants, markets, and supported sports through an OOMOL-connected The Odds API account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent query The Odds API through OOMOL's connector for sports, events, odds, scores, participants, and market metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends executing a remote installer script directly in a shell.

Mitigation: Before installation, prefer a safer vendor-supported install path, review the installer, and verify any available checksum or signature.

Risk: The skill depends on OOMOL's oo CLI and a connected The Odds API account.

Mitigation: Install only if comfortable with OOMOL's CLI and account connection model, and avoid exposing raw The Odds API credentials outside the connector.

## Reference(s):

- [The Odds API homepage](https://the-odds-api.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-the-odds-api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with oo CLI commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns read-only The Odds API data through OOMOL.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

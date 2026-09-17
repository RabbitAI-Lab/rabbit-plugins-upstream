## Description:

Supadata helps agents search and read Supadata-backed YouTube and web data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Supadata account details, YouTube channel, playlist, video, and transcript data, and web links or Markdown content without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that fetch and execute scripts.

Mitigation: Install the oo CLI only through a trusted, pinned, signed, or otherwise verified release channel, and require review before running curl-to-bash or irm-to-iex setup commands.

Risk: The skill depends on an authenticated OOMOL-connected Supadata account and may fail when credentials, scopes, app connection, or billing are unavailable.

Mitigation: Run setup or connection steps only after an action fails for the matching reason, and verify account connection and billing status before retrying.

## Reference(s):

- [ClawHub Supadata skill page](https://clawhub.ai/oomol/skills/oo-supadata)
- [Supadata homepage](https://supadata.ai/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supadata connector responses include data and meta.executionId fields when actions run successfully.]

## Skill Version(s):

1.0.4 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

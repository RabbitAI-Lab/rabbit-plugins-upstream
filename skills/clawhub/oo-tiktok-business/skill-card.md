## Description:

TikTok Business enables an agent to search and read TikTok Business data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, commerce teams, and agents acting for connected TikTok Business users use this skill to list advertisers and campaigns, inspect GMV Max resources, and retrieve reporting or eligibility data through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup asks users to run remote installer scripts directly in a shell.

Mitigation: Review or replace the installer flow with a safer verified installation method, such as an official signed package, pinned release, or locally reviewed installer before use.

Risk: TikTok Business data is accessed through OOMOL as an intermediary.

Mitigation: Use the skill only where sharing TikTok Business data through OOMOL is acceptable and the account connection has the intended scopes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-tiktok-business)
- [TikTok Business Homepage](https://business.tiktok.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL TikTok Business Connection](https://console.oomol.com/app-connections?provider=tiktok_business)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

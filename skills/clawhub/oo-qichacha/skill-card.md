## Description:

Qichacha helps agents inspect schemas and run Qichacha connector actions for business data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch Qichacha business registration data, including company shareholders and historical outbound investments, through an OOMOL-connected Qichacha account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute downloaded code during oo CLI installation.

Mitigation: Review the installer path first; prefer the official install guide, a pinned package, or a downloaded installer that can be verified before execution.

Risk: Normal use fetches business data through the user's OOMOL-connected Qichacha account.

Mitigation: Inspect the live connector schema before sending a payload and run only the required read action under the user's authorized account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-qichacha)
- [Qichacha OpenAPI](https://openapi.qcc.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown guidance with shell command examples; connector action responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

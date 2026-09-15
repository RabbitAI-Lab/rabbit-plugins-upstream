## Description:

Webshare helps agents read Webshare account profile, proxy configuration, proxy inventory, and hourly usage data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations users use this skill to inspect Webshare account and proxy data from an OOMOL-connected Webshare account. It supports read-oriented workflows such as profile checks, proxy listing, proxy configuration lookup, and hourly usage review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could execute unreviewed code.

Mitigation: Review setup instructions before installing; prefer a verified package or separately inspected installer; do not let an agent run the installer automatically.

Risk: Connector payloads can be incorrect if an action schema is assumed instead of checked.

Mitigation: Inspect the live action schema before each connector run and send only payloads that match the authoritative schema.

Risk: Future write or destructive connector actions could change Webshare state.

Mitigation: Ask the user to confirm the exact target, payload, and effect before running any write or destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-webshare)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Webshare Homepage](https://www.webshare.io/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; listed connector actions are read-oriented.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

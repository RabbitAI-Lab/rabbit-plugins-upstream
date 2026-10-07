## Description:

Create and improve Vibbit content by researching products, planning scripts, generating images, audio and video, producing and translating videos, and reviewing results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zgissing](https://clawhub.ai/user/zgissing)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and production teams use this skill to research products, develop creative concepts, generate or edit media with Vibbit, and review or localize finished videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be stored in an unencrypted local private file.

Mitigation: Prefer the host secret manager; if using the local helper, protect the private credentials file.

Risk: Cloud media generation can consume paid credits and transmit local media to Vibbit.

Mitigation: Review uploads and credit-consuming submissions before authorizing them.

Risk: Optional local rendering may install new dependencies through npx.

Mitigation: Review the renderer and dependency installation before approving it.

## Reference(s):

- [Vibbit Skills release](https://clawhub.ai/zgissing/skills/vibbit-skills)
- [Vibbit module catalog](artifact/references/catalog.md)
- [Vibbit authentication reference](https://vibbit.apifox.cn/514565013e0)
- [Vibbit API client guide](artifact/references/runtime/api-client.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Media files]

**Output Format:** [Markdown responses with media links or local deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud generation requires an authorized Vibbit account and may consume credits.]

## Skill Version(s):

2.14.5 (source: release evidence, skill metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

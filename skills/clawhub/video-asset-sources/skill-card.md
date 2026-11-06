## Description:

Find video, audio, motion, font, icon, logo, LUT, and HDRI assets through tested sources, check their licenses, and record required credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and editing agents use this skill to find fetchable media and design assets, check each item's usage terms, and keep a credits record for assets used in an edit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External search queries may expose confidential project details.

Mitigation: Use generic search terms and keep confidential project details out of queries, including the disclosed varg fallback.

Risk: Asset licenses and attribution requirements vary, and the credits script cannot establish permission.

Mitigation: Check the source item's actual license and required attribution before using each asset.

Risk: Optional installers, live services, and externally fetched package contents are outside the inspected bundle.

Mitigation: Review live service results and fetched contents; review and pin package versions before running optional installers.

## Reference(s):

- [ClawHub release](https://clawhub.ai/vargai/skills/video-asset-sources)
- [all-sources.md](artifact/references/all-sources.md)
- [tested-queries.md](artifact/references/tested-queries.md)
- [traps.md](artifact/references/traps.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files, JSON]

**Output Format:** [Markdown guidance and commands, fetched media assets, and a JSON credits record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Check each asset's license and attribution before use; the credits record does not establish permission.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

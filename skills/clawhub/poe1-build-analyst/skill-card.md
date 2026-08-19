## Description:

Generate, compare, and verify Path of Exile 1 builds for a specified patch or league. Use for PoE1 3.29 Curse of the Allflame recommendations, PoE Ninja build-statistics research, qpooqp777/pob-cli analysis, and early/mid/endgame passive trees, gem links, equipment targets, metrics, and PoB character codes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qpooqp777](https://clawhub.ai/user/qpooqp777)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, build analysts, and Path of Exile players use this skill to produce reproducible endgame PoE1 build analyses from PoE Ninja snapshots, public character data, or complete PoB character codes. It separates statistical observations, Path of Building calculations, manual recommendations, and unverified estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Helper scripts can be configured to run a local executable through the PoB command setting.

Mitigation: Use the default pob command or a trusted absolute path, and do not pass untrusted values to command-selection options.

Risk: Build or character data could be made public if a pobb.in upload is performed.

Mitigation: Generate private share codes with dry-run behavior by default, and require explicit confirmation before publishing any public URL.

Risk: Unavailable PoE Ninja data, missing PoB dependencies, invalid XML, or failed calculations can lead to misleading recommendations if treated as verified.

Mitigation: Record source status and calculation warnings, label blocked or unverified results clearly, and do not invent PoB metrics.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qpooqp777/skills/poe1-build-analyst)
- [Server-resolved source repository](https://github.com/qpooqp777/poe1-build-analyst)
- [API reference](references/api_reference.md)
- [Research notes](references/research_notes.md)
- [Path of Exile 3.29.0 announcement](https://www.pathofexile.com/forum/view-thread/3985332)
- [PoE Ninja PoE1 builds](https://poe.ninja/poe1/builds)
- [qpooqp777/pob-cli](https://github.com/qpooqp777/pob-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with JSON build records and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Endgame-only workflow; character codes remain private unless the user explicitly approves public publication.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

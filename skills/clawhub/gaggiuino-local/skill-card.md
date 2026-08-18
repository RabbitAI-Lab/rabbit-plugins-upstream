## Description:

Gaggiuino Local helps an agent interact with a local Gaggiuino espresso machine for machine status, shot analysis, profile management, settings work, maintenance history, shot graph rendering, and synchronized overlay videos.

This skill is for research and development only.

## Publisher:

[zackzmai](https://clawhub.ai/user/zackzmai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect and operate a trusted local Gaggiuino machine, analyze real or historical espresso shots, manage profiles/settings, and generate shot visualizations. It is especially useful for telemetry-grounded espresso troubleshooting and dial-in guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can talk to a real local Gaggiuino machine through a saved base URL.

Mitigation: Keep the saved endpoint pointed only at a trusted local/LAN device, inspect it with get-base-url when unsure, and clear it when moving networks.

Risk: Profile switches and settings writes can change machine behavior.

Mitigation: Require explicit user confirmation before profile switches or settings writes, read current machine state first, and verify by follow-up read when confirmation matters.

Risk: Shot analysis or image-based graph interpretation can produce incorrect dial-in guidance if telemetry or profile intent is incomplete.

Mitigation: Prefer real shot telemetry and embedded profile metadata; treat screenshots or weak graph evidence as provisional and ask the user to confirm the intended profile or family.

Risk: Video overlay synchronization can be wrong when audio is missing, noisy, or ambiguous.

Mitigation: Use manual sync offsets or audio diagnostics when automatic synchronization is uncertain.

## Reference(s):

- [Skill Page](https://clawhub.ai/zackzmai/skills/gaggiuino-local)
- [Analysis Protocol](references/analysis-protocol.md)
- [Dial-In Basics](references/dial-in-basics.md)
- [Extraction Levers](references/extraction-levers.md)
- [Profile Descriptions](references/profile-descriptions.md)
- [Profile Families](references/profile-families.md)
- [Profile Mapping](references/profile-mapping.md)
- [Shot Graph Analysis](references/shot-graph-analysis.md)
- [Troubleshooting](references/troubleshooting.md)
- [Espresso Aficionados Guides](https://espressoaf.com/guides)
- [Gaggiuino Community Profiles](https://github.com/Zer0-bit/gaggiuino/tree/community/profiles)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown responses with JSON/tool output, shell commands, configuration guidance, generated PNG/MP4 shot graphs, and overlay video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Rendering scripts may create static shot graphs, animated shot graphs, and synchronized overlay videos under ~/.openclaw/workspace/gaggiuino-output.]

## Skill Version(s):

3.2.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

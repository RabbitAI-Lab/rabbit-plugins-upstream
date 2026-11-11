## Description:

Helps creators keep AI video characters and hero props consistent through detailed passports, visual and voice references, reusable prompts, and optional code-based routes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and developers use this skill to define consistent characters and hero props before generating AI video, then carry those specifications through stills and shots. It guides the creation of passports, visual and voice references, shot prompts, and optional code-based rigs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flagged an unauthenticated renderer with a possible directory traversal issue, unclear capabilities and data sharing, and a partial scan.

Mitigation: Avoid installation until the renderer exposure and capability disclosure are addressed; review the execution surface and the assets sent to external services.

Risk: Security guidance flags moderation workarounds and unpinned package instructions.

Mitigation: Review those instructions before use and verify or pin package sources; do not use any steps that bypass safeguards.

## Reference(s):

- [Project homepage (Clawdis metadata)](https://github.com/vargHQ/skills/tree/main/character-passport)
- [Blind-judged test write-up](https://claude.ai/artifact/AJ1g4Qren3ZvwERSwrQigt)
- [Passport format](artifact/references/passport.md)
- [Turnaround and expression sheets](artifact/references/sheets.md)
- [Code routes](artifact/references/code.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Image and voice prompts, Image assets, Code, Shell commands]

**Output Format:** [Markdown specifications and prompts, image and voice references, and optional Python, TypeScript, or HTML code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs vary by workflow; image and voice generation may use external services.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

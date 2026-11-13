## Description:

Guides agents to find usable footage, audio, graphics, and other video assets, check each item's license, and record required credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and video editors use this skill to source footage, music, sound effects, graphics, fonts, and other assets for an edit while checking usage terms and keeping required credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports a scope mismatch and unpinned installation commands.

Mitigation: Review the skill's intended scope and inspect and pin the release before installation.

Risk: Using reference-search features can send project-derived queries to an external service.

Mitigation: Review the external-search behavior and avoid including sensitive project details in queries.

Risk: The security guidance says two local references could not be resolved, leaving scan evidence incomplete.

Mitigation: Inspect the relevant references directly before relying on their recommendations.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/vargai/skills/video-asset-sources)
- [Publisher profile](https://clawhub.ai/user/vargai)
- [Project homepage](https://github.com/vargHQ/skills/tree/main/video-asset-sources)
- [Tested asset sources](references/all-sources.md)
- [Tested queries](references/tested-queries.md)
- [Source traps and limitations](references/traps.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Media files, Credits metadata]

**Output Format:** [Markdown guidance and shell commands, downloaded media assets, and a JSON credits file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asset types vary by request; credits record each asset's source and license.]

## Skill Version(s):

1.0.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

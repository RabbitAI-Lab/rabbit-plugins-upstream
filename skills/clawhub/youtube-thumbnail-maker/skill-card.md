## Description:

Proposes three YouTube thumbnail directions, renders the selected 16:9 design through Beatra, and provides title-matching and channel-style guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

YouTube creators and their teams use this skill to compare thumbnail concepts, render a chosen image from a topic or supplied visual, and keep titles and channel styling consistent. Rendering requires a connected Beatra account with credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Beatra stores a broadly scoped account token locally.

Mitigation: Connect only if comfortable with the account access and keep the stored credential private.

Risk: Selected source images and package or platform metadata are sent to Beatra.

Mitigation: Use only images and metadata you are comfortable sharing with Beatra.

Risk: The package silently updates its local code by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if changes should require an explicit action.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/youtube-thumbnail-maker)
- [Beatra skill homepage](https://beatra.ai/skills/youtube-thumbnail-maker)
- [Thumbnail workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown guidance, Image artifact links]

**Output Format:** [Markdown with selected thumbnail artifact links and task details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Three text directions precede the selected paid render; the default image canvas is 16:9.]

## Skill Version(s):

0.2.6 (source: server-resolved ClawHub release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

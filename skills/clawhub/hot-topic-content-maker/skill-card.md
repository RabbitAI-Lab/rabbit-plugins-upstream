## Description:

Turns a trending topic into account-specific social post angles, a caption, hashtags, a rendered cover, and optionally a narrated short clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and social media teams use this skill to turn a timely topic into a brand-relevant post, with an optional short video for social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Beatra grants broad account authority for paid media generation.

Mitigation: Review the requested access and approve each paid lookup or generation before submitting it.

Risk: The bundled client automatically installs verified skill updates without separate approval by default.

Mitigation: Review the update policy and disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if manual review is required.

Risk: The shared Beatra credential can authorize other Beatra skills if exposed.

Mitigation: Protect `~/.beatra/credentials.json` as a sensitive shared credential and disconnect when no longer needed.

## Reference(s):

- [ClawHub release](https://clawhub.ai/beatra-ai/skills/hot-topic-content-maker)
- [Hot topic workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Installation and authentication](references/installation-and-auth.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Images, Video]

**Output Format:** [Post copy and plan in Markdown, rendered cover image, and optional narrated vertical video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cover-only by default; optional clip and paid trend lookups require separate approval.]

## Skill Version(s):

0.2.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

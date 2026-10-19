## Description:

Creates singable school-event lyrics from a school's details and can turn approved lyrics into a finished vocal song or an optional instrumental piece.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, students, and school organizers use it to draft and revise class songs, graduation songs, welcome songs, and anthems from supplied school details, then optionally request a generated recording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client uses a shared, full-scope Beatra device credential across installed Beatra skills.

Mitigation: Install only if comfortable with shared account access; keep the credential private and review authorization before connecting.

Risk: Installation can register telemetry and send user-provided content to Beatra for generation.

Mitigation: Review what is shared and avoid including sensitive school or student details unless authorized.

Risk: Silent automatic updates can replace bundled package code without a separate prompt.

Mitigation: Disable automatic updates if unapproved package changes are unacceptable, and review updates before enabling them.

Risk: Uninstall actions can affect a connection shared with other Beatra skills.

Mitigation: Use the documented uninstall flow and check whether other Beatra skills still need the shared connection.

Risk: Music generation consumes credits and retries may create additional paid work.

Mitigation: Approve the current price and each generation slot before submission; recover uncertain requests using the original request identity.

## Reference(s):

- [ClawHub release](https://clawhub.ai/beatra-ai/skills/school-song-maker)
- [School song workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Audio links]

**Output Format:** [Markdown lyric sheet and production guidance; links and details for generated audio when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lyrics can be delivered without paid generation; generated songs may include multiple takes. No sheet music or vocal/accompaniment separation.]

## Skill Version(s):

0.1.1 (source: ClawHub release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

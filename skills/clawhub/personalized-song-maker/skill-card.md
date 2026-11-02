## Description:

Turn a person's story and occasion into original lyrics and a newly generated song.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can turn a recipient's story and occasion into approved lyrics and one original personalized song, such as a birthday, wedding, anniversary, or tribute song.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared account authorization extends beyond song creation to other media generation and voice management.

Mitigation: Review the requested permissions before connecting and revoke the device through Beatra Console when access is no longer needed.

Risk: Approved lyrics and production prompts are sent to Beatra, and installation analytics are collected automatically; personal story details may be sensitive.

Mitigation: Remove sensitive story details before submission and share only information needed for the song.

Risk: Each song generation consumes credits.

Mitigation: Approve the exact inputs and paid generation before submitting.

## Reference(s):

- [Story-to-song workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Updates and security](references/updates-and-security.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/personalized-song-maker)

## Skill Output:

**Output Type(s):** [Text, Markdown, Audio]

**Output Format:** [Markdown lyrics and production details with a generated song audio artifact or link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One approved lyric draft and one song generation per run; generation is paid.]

## Skill Version(s):

0.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

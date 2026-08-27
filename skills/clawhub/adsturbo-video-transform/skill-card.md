## Description:

Transforms an existing video by swapping the on-screen person, driving a static portrait with reference motion, or translating and re-dubbing the video with lip sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit authorized media to AdsTurbo for campaign-oriented character swaps, motion-driven portrait animation, and translated or re-dubbed video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads media to public URLs and sends media to a third-party AdsTurbo service.

Mitigation: Use only media, voices, and likenesses the user is authorized to process; avoid private or confidential content unless AdsTurbo account terms, storage visibility, retention, and sharing settings are acceptable.

Risk: Character swap, motion control, and lip-sync translation can transform a person's likeness or voice in misleading or non-consensual ways.

Mitigation: Confirm consent and intended use before processing identifiable people, and avoid non-consensual identity, likeness, or voice transformations.

Risk: Async task timeouts can lead to accidental resubmission and duplicate charges.

Mitigation: Resume polling with the existing workspace ID after a timeout and use idempotency keys when retrying after network interruptions.

## Reference(s):

- [AdsTurbo Video Transform](references/video_transform.md)
- [Upload](references/upload.md)
- [Work Status](references/work.md)
- [AdsTurbo API key signup](https://adsturbo.ai?channel=clawhub)
- [AdsTurbo API base URL](https://adsturbo.ai/klian/novartapi)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces public media URLs, asynchronous workspace IDs, status responses, and result URLs from AdsTurbo API operations.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

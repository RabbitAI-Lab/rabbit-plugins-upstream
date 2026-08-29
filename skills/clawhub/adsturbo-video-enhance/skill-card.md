## Description:

Clean up a video without changing its content: remove watermarks, logos and burnt-in subtitles, upscale to 2K/4K, add or translate subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to clean existing video assets by removing visible clutter or burnt-in text, increasing resolution, and adding or translating subtitles while keeping the visual content unchanged.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media can be sent to AdsTurbo and converted into a public URL.

Mitigation: Use only non-sensitive videos that the user owns or is authorized to process, and confirm the service's retention and access terms before uploading confidential or regulated media.

Risk: Watermark, logo, or burnt-in subtitle removal can remove attribution or other context markers.

Mitigation: Confirm the user has rights to modify the media and that removal does not misrepresent ownership, provenance, or required disclosures.

Risk: Asynchronous tasks may continue running after a local timeout, and resubmission can create duplicate work or charges.

Mitigation: Resume polling by workspace ID after timeout and use stable idempotency keys when retrying submissions.

## Reference(s):

- [Video Enhance](references/video_enhance.md)
- [Upload](references/upload.md)
- [Work Status](references/work.md)
- [ClawHub Skill Page](https://clawhub.ai/adsturbo/skills/adsturbo-video-enhance)

## Skill Output:

**Output Type(s):** [Text, Shell commands, API calls, Guidance]

**Output Format:** [Markdown or plain text guidance with shell commands; API responses are JSON objects that include task status and result URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce public media URLs and AdsTurbo workspace IDs for asynchronous task tracking.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

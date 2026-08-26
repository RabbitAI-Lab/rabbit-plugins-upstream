## Description:

Swap out one element of a video: replace the on-screen person, drive a static portrait with a reference video's motion, or translate the whole video into another language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to transform existing videos by swapping an on-screen person, animating a portrait with reference motion, or re-dubbing a video into another language with lip sync.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload personal, customer, employee, or biometric media to AdsTurbo and produce generated public URLs.

Mitigation: Use only media that the user has rights and consent to transform, avoid sensitive inputs unless the AdsTurbo processing terms are acceptable, and treat returned asset URLs as shareable links.

Risk: Realistic person, motion, voice, and lip-sync transformations can misrepresent a person's likeness or speech.

Mitigation: Confirm the user has permission for the person or voice being transformed and avoid creating misleading or non-consensual impersonation content.

Risk: The release evidence reports unpinned Python dependencies.

Mitigation: Install in an isolated environment and consider pinning dependencies before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adsturbo/skills/adsturbo-video-transform)
- [Upload reference](references/upload.md)
- [Video transform reference](references/video_transform.md)
- [Work status reference](references/work.md)
- [AdsTurbo website](https://www.adsturbo.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and generated video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit asynchronous AdsTurbo jobs and return public URLs for uploaded assets or generated video results.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

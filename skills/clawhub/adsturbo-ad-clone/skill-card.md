## Description:

Clone a competitor ad: auto-storyboard it into shots and prompts, then regenerate a new video with the same structure; it can also run analysis only, with no generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, creative teams, and agent operators use this skill to analyze a public reference ad, extract a storyboard and prompt, and generate a new AdsTurbo video with a similar structure. It can also be used for shot-by-shot competitor ad analysis without generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media is sent to AdsTurbo and made available by URL, which can expose private, confidential, regulated, copyrighted, or likeness-sensitive content.

Mitigation: Use only assets you have rights and consent to process, prefer already-public or approved media, and avoid uploading sensitive or restricted material.

Risk: Reference videos must be public URLs or uploaded first, so local files cannot be processed privately in place.

Mitigation: Convert local media through the documented upload flow only when public URL handling is acceptable for the asset.

Risk: Polling timeouts can lead to duplicate paid generation if the task is resubmitted while still running.

Mitigation: Resume with the returned workspace ID or use idempotency keys for retries instead of submitting the same generation again.

## Reference(s):

- [Ad Clone](references/ad_clone.md)
- [Upload](references/upload.md)
- [Work Status](references/work.md)
- [ClawHub Skill Page](https://clawhub.ai/adsturbo/skills/adsturbo-ad-clone)
- [AdsTurbo API Key Signup](https://adsturbo.ai?channel=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return structured shot analysis, clone prompts, workspace IDs, uploaded public URLs, task status, or final result URLs depending on the selected command.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

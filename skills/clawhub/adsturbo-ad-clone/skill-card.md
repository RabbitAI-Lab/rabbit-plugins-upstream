## Description:

Clone a competitor ad by turning a reference video into a shot breakdown and prompt, then generating a new video with the same structure; the skill can also run analysis without generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, creative teams, and developers use this skill to analyze a reference ad, turn it into a shot-by-shot prompt, and generate a new video with a similar structure. It can also inspect an ad for analysis without generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos, images, or audio are sent to AdsTurbo and may be returned as public URLs.

Mitigation: Use only media that the user has rights and consent to process, and avoid sensitive personal or biometric content unless the user explicitly accepts that exposure.

Risk: Cloned ad structure can create intellectual property, brand, or likeness concerns when the reference material belongs to another party.

Mitigation: Confirm the user has the rights to use the reference and steer outputs toward original creative expression rather than copying protected assets.

Risk: Timed-out generation or inspection tasks may still be running, and resubmitting can create duplicate charges.

Mitigation: Resume polling with the workspace ID or use an idempotency key when retrying after network issues.

Risk: The Python dependency list does not pin the requests package version.

Mitigation: Pin or otherwise constrain requests before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adsturbo/skills/adsturbo-ad-clone)
- [AdsTurbo](https://www.adsturbo.ai)
- [Ad Clone reference](references/ad_clone.md)
- [Upload reference](references/upload.md)
- [Work Status reference](references/work.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; script results are JSON containing analysis, prompts, workspace IDs, status, or result URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ADSTURBO_API_KEY; source media must be public URLs or uploaded first.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

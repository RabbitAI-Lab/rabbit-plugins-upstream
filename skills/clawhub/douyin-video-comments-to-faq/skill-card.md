## Description:

Turns seller-answered Douyin comments into a set of individual FAQ stills for listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers use the skill to plan and create FAQ stills from public Douyin questions and their own confirmed product answers, with separate approval for paid comment lookup and image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra package requests a shared device-wide token with broad media and wallet-related authority.

Mitigation: Install only if comfortable with that access; review account activity and revoke the device in Beatra Console when no longer needed.

Risk: The package silently installs updates by default.

Mitigation: Disable automatic updates using the documented command if release-by-release review is required.

Risk: Paid lookups and image jobs can incur charges.

Mitigation: Review the live cost and explicitly approve each paid stage before submission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/douyin-video-comments-to-faq)
- [Douyin comment FAQ workflow](references/workflow.md)
- [Comment lookup](references/comment-lookup.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Markdown, Images, Guidance]

**Output Format:** [Markdown FAQ plan and generated image stills]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically four to eight one-question, one-answer stills; image delivery follows seller approval and reports actual charges.]

## Skill Version(s):

0.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

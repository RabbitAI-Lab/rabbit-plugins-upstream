## Description:

Turns a TikTok creator's public profile and recent posts, together with already-written collaboration terms, into a set of individual brief stills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Media buyers use the skill to plan and produce a handoff-ready set of creator collaboration brief stills from a chosen TikTok profile and terms they have already written.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent shared Beatra device token grants broad media and wallet-related access.

Mitigation: Review the requested permissions before connecting, protect the local credential, and disconnect when access is no longer needed.

Risk: Local image files can be uploaded to Beatra.

Mitigation: Inspect each file and obtain explicit permission before uploading it.

Risk: The installed package silently checks for and installs updates by default.

Mitigation: Review update behavior before installation; disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if unattended changes are unacceptable.

Risk: Creator lookups and image stages can consume credits, including separate charges for additional pages or edits.

Mitigation: Check the live credit price and obtain separate approval for each paid stage; recover uncertain requests using the original request identity rather than creating duplicate charges.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/tiktok-creator-to-brief-stills)
- [Beatra skill homepage](https://beatra.ai/skills/tiktok-creator-to-brief-stills)
- [Brief still workflow](references/workflow.md)
- [Creator lookup](references/creator-lookup.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Image files, Guidance]

**Output Format:** [A labeled lookup memo and still list, followed by individual generated image stills with reported dimensions and charges when approved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normally four to eight stills; paid lookups and image generation require separate approval.]

## Skill Version(s):

0.1.8 (source: ClawHub release and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

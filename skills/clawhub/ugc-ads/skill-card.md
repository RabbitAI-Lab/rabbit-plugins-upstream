## Description:

Generate handheld, vertical phone-shot UGC clips with imperfect framing, practical lighting, no cinematic grading, and no beauty filters so product videos read as customer-shot rather than agency-made.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketers, and agents use this skill to brief and generate synthetic customer-style product clips such as unboxings, first impressions, and simple review videos through Ofox. It is intended for disclosed synthetic or dramatized advertising workflows, not undisclosed endorsements or fake testimonials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Synthetic customer-style clips may be mistaken for real reviews or endorsements.

Mitigation: Use the skill only for synthetic or dramatized ads that will be disclosed as advertising or AI-generated content.

Risk: Product photos or brief details may contain confidential, personal, or regulated information sent to Ofox for processing.

Mitigation: Review inputs before upload and avoid sending confidential product photos, personal data, or regulated content unless that processing is acceptable.

Risk: Overbroad or unpinned dependency installation can pull more skills than required.

Mitigation: Install only the required ofox-video-core dependency from a trusted, pinned source where possible.

Risk: The skill's UGC steering has limited run evidence and can silently produce clips that look too polished or include unintended camera-device objects.

Mitigation: Review generated frames before use, start with small paid drafts, and follow the skill's prompt checks for anti-polish wording and visible-device exclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/ugc-ads)
- [Ofox app and API key setup](https://app.ofox.ai)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands and generated video file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY plus curl and jq; generated videos are downloaded as files by the delegated Ofox video workflow.]

## Skill Version(s):

1.0.0 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

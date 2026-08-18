## Description:

Retrieves translated patent titles and abstracts from the Zhihuiya (PatSnap) patent database in Chinese, English, or Japanese by patent ID or publication number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, patent analysts, and developers use this skill to fetch translated patent titles and abstracts for known patent IDs or publication numbers, including batch lookups and optional family-patent abstract fallback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use API keys and guide users through phone/SMS login that may generate or reveal API tokens.

Mitigation: Prefer self-service account setup, avoid sharing one-time codes or tokens in chat transcripts, and rotate exposed API keys.

Risk: Patent identifiers and session metadata may be sent to remote LinkFox and PatSnap-related services.

Mitigation: Review endpoint environment variables and avoid submitting confidential patent identifiers unless the destination service is approved for that data.

Risk: The onboarding flow can create payment orders when quota or billing errors occur.

Mitigation: Require explicit user confirmation before listing paid plans or creating an order, and verify the selected plan and payment method.

Risk: Full API responses are saved locally and may contain patent query results or other sensitive context.

Mitigation: Treat saved LinkFox response files as sensitive, keep them in approved workspaces, and remove them when no longer needed.

Risk: The skill can submit feedback externally about results or user sentiment.

Mitigation: Review feedback content before submission and omit confidential user or patent details unless sharing is approved.

## Reference(s):

- [API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-abstract-data-translated)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown tables and JSON, with full API responses saved as local JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports batch patent identifiers, Chinese/English/Japanese translation targets, optional family-patent fallback, and a 24-hour local cache.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

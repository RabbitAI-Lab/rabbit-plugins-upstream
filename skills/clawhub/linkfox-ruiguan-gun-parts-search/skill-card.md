## Description:

Screens product image URLs with Ruiguan visual similarity search to identify potential matches against known policy-violating products.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and compliance reviewers use this skill to pre-screen product images before listing or review. It helps identify visually similar known violations, but it does not provide a final legal or platform-policy determination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product image URLs, and local images uploaded to obtain public URLs, are sent to LinkFox/Ruiguan for compliance screening.

Mitigation: Use only images whose third-party processing and temporary public-link exposure are acceptable; avoid private, signed, proprietary, or regulated images.

Risk: Full API responses and cache files may be stored locally, including submitted image URLs, matched violation images, product titles, detection IDs, and token cost data.

Mitigation: Review local retention and access controls for the generated linkfox data and cache directories, and remove stored responses when they are no longer needed.

Risk: The skill includes account, token, and billing helpers, and normal detection calls consume credits.

Mitigation: Confirm expected credit use before repeated calls, review any onboarding or payment action before running it, and keep API keys out of shared logs or transcripts.

Risk: Endpoint override environment variables can redirect requests away from the default LinkFox endpoints.

Mitigation: Leave endpoint overrides unset unless the destination is explicitly trusted and approved for the data being processed.

Risk: Similarity matches are screening signals, not definitive policy or legal rulings.

Mitigation: Treat high-similarity results as triage findings and verify final decisions against the applicable marketplace or platform policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-ruiguan-gun-parts-search)
- [Ruiguan image compliance API reference](references/api.md)
- [Authentication and billing onboarding reference](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON/API result summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a publicly reachable imageUrl up to 1000 characters. Small responses may be printed in full; larger responses are summarized while the complete JSON response is saved locally.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

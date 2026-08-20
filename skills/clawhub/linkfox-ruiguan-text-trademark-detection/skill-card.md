## Description:

Helps e-commerce sellers scan product titles and listing text for text-based trademark matches and potential infringement risk across supported regions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers and marketplace operators use this skill to check product titles, descriptions, and bullet points for text trademark risks before publishing listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product titles and descriptions are sent to LinkFox/Ruiguan for trademark analysis.

Mitigation: Avoid including secrets, customer personal data, or sensitive unpublished listing details unless the user is comfortable sharing them with the provider.

Risk: The skill includes LinkFox account, API-key, and payment-credit workflows.

Mitigation: Prefer the provider's self-service account portal when possible and treat printed API keys and payment artifacts as sensitive.

Risk: Trademark responses and cache files may be retained locally under linkfox session directories.

Mitigation: Clean up saved response and cache files when they are no longer needed.

Risk: Trademark scan results are risk signals rather than legal clearance.

Mitigation: Present results as reference information and recommend consulting an IP attorney for definitive trademark advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-ruiguan-text-trademark-detection)
- [Ruiguan text trademark detection API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown risk summaries and tables, shell commands, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under linkfox session directories; large responses print summaries unless inline output is requested; repeated parameter sets may use a 24-hour local cache.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

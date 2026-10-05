## Description:

Analyzes pet images or videos to estimate breed or body type and fur density, then recommends a drying temperature and duration curve for pet care, not medical use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, groomers, and developers of pet-drying devices can use a pet image or video to obtain suggested drying temperatures and durations and view prior analysis reports. Recommendations are for pet care rather than medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, or media URLs are sent to external lifeemergence.com services.

Mitigation: Only submit media you are authorized to share; review the provider's privacy and retention terms before use.

Risk: The skill silently creates or reuses a local identity and stores backend session tokens in a workspace SQLite database.

Mitigation: Run in a constrained workspace and restrict access to its local database and stored credentials.

Risk: Prior cloud reports may be queried with limited user control.

Mitigation: Limit access to report history and avoid sharing report links or contents without authorization.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-adaptive-pet-drying-temperature-analysis)
- [Pet drying recommendation API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or JSON, with an optional saved file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes suggested temperature (°C) and duration (minutes), analysis results, and report links when available.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

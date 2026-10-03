## Description:

Analyzes pet rest-area videos to report sleep duration, position changes, awakenings, and a sleep-quality score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers use this skill to assess nighttime sleep patterns from pet-bed video and review prior analysis reports. Results may help flag changes worth discussing with a veterinarian, but are not a diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet rest-area footage or video URLs are sent to lifeemergence.com services.

Mitigation: Share footage only if comfortable with the provider's retention and deletion practices; avoid private household or clinical footage until these are understood.

Risk: The skill automatically creates or reuses an identity, stores tokens locally, and retrieves cloud report history with limited user-facing control.

Mitigation: Review the local data directory for generated SQLite and token files, and consider the account-linked cloud history before use.

## Reference(s):

- [Pet sleep analysis API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table; optional JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a report link, sleep metrics, a 0–100 score, and recommendations.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

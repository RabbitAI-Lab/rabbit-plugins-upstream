## Description:

Detects morbid behavioral cues in poultry and pigs from continuous barn videos, including difficulty standing, ruffled feathers or piloerection, isolation, drowsiness, and appetite loss, and returns behavior types with risk levels for early screening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, veterinarians, and monitoring agents use this skill to screen poultry and swine barn images or videos for early behavioral warning signs. The output supports inspection and escalation workflows, but it is not a veterinary diagnosis or treatment recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends barn videos, video URLs, and report queries to a configured remote service.

Mitigation: Install and use it only when that data sharing is acceptable for the farm, user, and deployment environment.

Risk: The bundled configuration includes development HTTP endpoints as well as production HTTPS endpoints.

Mitigation: Review configuration before use and confirm it targets the intended HTTPS production service.

Risk: The skill creates or reuses a local identity and stores service tokens in the workspace data database.

Mitigation: Limit workspace access, review token storage expectations, and rotate or clear local credentials according to site policy.

Risk: Behavior screening results could be mistaken for veterinary diagnosis or treatment advice.

Mitigation: Use results as early-screening support and confirm disease or medication decisions with a veterinarian and appropriate testing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-sick-poultry-behavior-detect-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or JSON text returned from API-backed behavior analysis, with optional saved report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [History queries render Markdown tables with report names, risk levels, analysis times, and report links.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

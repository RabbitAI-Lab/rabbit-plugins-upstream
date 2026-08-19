## Description:

Analyzes pet drying box video files or URLs through a remote service to identify early heat-stress signals such as panting intensity, tongue color, and body movement, then returns risk levels, intervention suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet care businesses, grooming shops, and veterinary teams use this skill to submit pet drying box video evidence and receive structured heat-stress risk observations and suggested safety interventions. The output is for drying safety support and is not a veterinary diagnosis or treatment plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos, URLs, and generated analysis reports are processed by the remote lifeemergence.com service.

Mitigation: Use only footage that is appropriate for that service, and review its retention, access, and privacy policies before using clinic, home, customer, or internal-camera video.

Risk: The skill can silently create or reuse a local service identity and store authentication tokens in a workspace SQLite database.

Mitigation: Run the skill in an isolated workspace, restrict access to local data stores, and clear stored identities or tokens when the analysis workflow is complete.

Risk: History queries retrieve cloud report records associated with the resolved local identity.

Mitigation: Avoid shared workspaces for sensitive use, and confirm which service identity is active before querying historical reports.

Risk: Heat-stress output can be mistaken for veterinary diagnosis or treatment advice.

Mitigation: Treat results as drying safety observations; for high-risk or urgent signs, stop drying, cool and ventilate the pet, and involve qualified veterinary care when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-drying-box-heat-stress-analysis)
- [Pet drying box API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, guidance]

**Output Format:** [Structured report text or JSON, with Markdown tables or links for history queries and an optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include remote report export links; local file inputs are limited to mp4, avi, or mov videos up to 10 MB.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata; artifact frontmatter and changelog mention 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

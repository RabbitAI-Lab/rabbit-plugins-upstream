## Description:

Analyzes reference-calibrated fish fry images or video to measure body length, estimate growth rate, build growth curves, and report unreliable measurements or growth concerns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External aquaculture operators, ornamental fish breeders, and lab users use this skill to analyze fish fry tank media that includes a known-size reference object, produce body-length and growth-rate reports, and review prior growth measurements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends images, videos, or media URLs to a remote analysis service.

Mitigation: Use it only when the publisher and service destination are trusted, and avoid submitting sensitive or regulated media unless that transfer is approved.

Risk: The skill creates or reuses an internal identity and stores API tokens in a local SQLite database.

Mitigation: Run it in a dedicated workspace, review local data retention expectations, and remove stored credentials or database files when access is no longer needed.

Risk: The default configuration includes developer network endpoints.

Mitigation: Confirm the configured service URLs before production use and replace private or development endpoints with approved production endpoints.

Risk: Measurement results can be unreliable when the reference object is missing, out of plane, low confidence, occluded, or captured from the wrong angle.

Mitigation: Require a known-size reference object in the same plane as the fish fry, use strict top-down high-resolution imagery, and return an unreliable-measurement status rather than a growth alert when confidence is insufficient.

Risk: Growth-management suggestions could be mistaken for disease diagnosis, medication guidance, or automatic device control.

Mitigation: Limit outputs to visual measurement, neutral husbandry suggestions, and professional referral; do not provide drug names, doses, feed brands, or unauthorized equipment actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-fry-growth-measurement-analysis)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files, guidance]

**Output Format:** [Markdown or JSON analysis report with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include body-length measurements, growth rates, population statistics, growth-curve links, recommended actions, and measurement-reliability status.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

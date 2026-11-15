## Description:

Through fixed aquarium cameras, the system analyzes fish behavior videos and detects abnormal frictional actions between fish bodies and tank walls, substrate, or rockwork — 'flashing' (fish flipping sideways and brushing tank walls rapidly) and 'scraping' (fish belly/flank rubbing on substrate). The system counts abnormal contact frequency per minute.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, aquaculture operators, and aquarium care teams use the skill to review fish video for frequent flashing or scraping and receive a structured behavior report with risk warnings and suggested observations. The warnings are behavioral indicators and do not confirm a parasite diagnosis; the skill documentation directs users to seek veterinary examination for confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags account and token handling beyond the skill's stated aquarium-analysis purpose.

Mitigation: Review how accounts are created or reused and how tokens are handled before installing.

Risk: Remote-service behavior may involve sharing aquarium footage; the security guidance calls for checking footage-sharing terms.

Mitigation: Review the service's footage-sharing terms and submit only footage you are permitted to share.

Risk: The security guidance warns that `--export-env-only` may still start processing.

Mitigation: Do not rely on that option as a no-processing safeguard; inspect the behavior and avoid running the skill unless the processing is acceptable.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-fish-flashing-scraping-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON analysis reports, Markdown summaries and history tables, and written guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include observed behavior counts, warning levels, suggested actions, caveats, and optional report links. Findings depend on the supplied video and are not a veterinary diagnosis.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

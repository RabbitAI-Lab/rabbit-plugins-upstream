## Description:

Analyzes fixed aquarium camera media to detect flashing and scraping behavior, count abnormal friction events, and produce ectoparasite risk warnings without diagnosing a specific disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners, aquaculture operators, public aquarium staff, and developers can use this skill to submit fish tank video or image inputs for structured flashing/scraping risk reports and history lookup. The skill is intended to warn about behavior patterns that may require closer observation or veterinary microscopy, not to provide medical diagnosis or treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium media and report metadata are sent to a third-party vendor service for analysis and history retrieval.

Mitigation: Use only with media the user is comfortable uploading, disclose the vendor service path, and require explicit consent before analysis or history lookup.

Risk: The skill can create or reuse local account identity state and store service tokens in a workspace SQLite database.

Mitigation: Run in an isolated workspace, review local data storage before deployment, and clear stored identity or token state when the skill is no longer needed.

Risk: The behavior analysis may be mistaken for a veterinary diagnosis or treatment recommendation.

Mitigation: Keep outputs framed as risk warnings, avoid specific disease diagnosis or drug/dose instructions, and direct users to qualified veterinary microscopy for confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-flashing-scraping-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-formatted structured analysis reports with optional shell commands for running the skill scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include friction event counts, alert level, recommended observation actions, disclaimers, and report links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

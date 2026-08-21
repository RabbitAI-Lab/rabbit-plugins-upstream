## Description:

Identifies individual livestock (pigs, cattle, sheep) by facial or body-pattern features and outputs a stable individual ID with confidence for precision farm management and tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and farm operations users use this skill to submit livestock images, videos, or media URLs for individual animal identification, confidence scoring, and report lookup. The skill supports identity-linked workflows for precision feeding, health tracking, production records, and breeding-stock management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Livestock media or media URLs are sent to remote analysis services.

Mitigation: Use only media that the operator is authorized to process, review the service destination before use, and avoid sending sensitive farm data until endpoint and data-handling requirements are confirmed.

Risk: The skill can silently create or reuse a local account identity and store authentication tokens in workspace data.

Mitigation: Run the skill in an isolated workspace, restrict access to local data files, and clear or rotate stored credentials after evaluation or tenant changes.

Risk: Bundled configuration includes development HTTP endpoints on 192.168.1.234.

Mitigation: Verify and replace development endpoints with approved production HTTPS endpoints before processing sensitive media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-individual-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands]

**Output Format:** [Markdown or JSON analysis output, including individual IDs, confidence values, matched feature details, report links, and optional history tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May process local media files or media URLs and can write results to a file when an output path is provided.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

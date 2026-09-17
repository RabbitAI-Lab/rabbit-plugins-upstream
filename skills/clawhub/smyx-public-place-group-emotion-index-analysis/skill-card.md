## Description:

Analyzes public-place camera images or video to produce anonymous group-level emotion distributions, a 0-100 group emotion index, regional breakdowns, and operational or safety suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Venue operators, safety teams, and developers use this skill to analyze authorized public-place footage for anonymous group-level emotion trends, customer-experience signals, and human-reviewed operational or safety recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public-camera footage is processed through configured cloud APIs.

Mitigation: Use only authorized footage, confirm public notice and legal basis, and limit retained data to approved aggregate reports.

Risk: The server security summary flags unsafe HTTP/debug defaults in configuration.

Mitigation: Review configuration before installation and replace test or HTTP endpoints with approved HTTPS production endpoints.

Risk: The server security summary flags silent local identity creation, stored tokens, and local identity database use.

Mitigation: Review local storage and access controls, rotate or remove tokens according to policy, and avoid exposing identity values in reports.

Risk: Group emotion outputs could be misused for individual decisions or automated interventions.

Mitigation: Use outputs only as anonymous group-level decision support with human review; do not use them for identity recognition, tracking, pricing, or individual treatment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-public-place-group-emotion-index-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON report text with optional saved output file and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs aggregate emotion metrics, region summaries, suggestions, and historical report listings from configured cloud APIs.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter: 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

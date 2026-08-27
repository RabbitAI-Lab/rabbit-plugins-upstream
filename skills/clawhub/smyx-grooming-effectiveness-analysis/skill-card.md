## Description:

Analyzes pet grooming images or videos to estimate coat matting, shed-hair volume, grooming effectiveness, hairball risk, and related history reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, groomers, and pet-care teams use this skill to review grooming-session media and receive structured care-oriented observations about matting, loose hair, grooming effect, hairball risk, and prior reports. The output is for pet-care reference and is not a medical diagnosis or treatment plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media, media URLs, and identity data may be sent to configured backend services.

Mitigation: Use only media and URLs appropriate for the configured service, and avoid sensitive media or internal URLs unless backend destination, retention, token handling, and cleanup controls are documented.

Risk: The skill can create or reuse account identifiers and store tokens locally.

Mitigation: Review local identity and token storage behavior before installation, and deploy only in environments where that account-handling model is acceptable.

Risk: Hairball-risk and grooming-effectiveness outputs are care-oriented estimates, not clinical findings.

Mitigation: Present results as grooming guidance and route medical concerns or abnormal symptoms to a qualified veterinary professional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-grooming-effectiveness-analysis)
- [ClawHub publisher profile](https://clawhub.ai/user/18072937735)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet grooming analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured text with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis depends on user-provided image or video input, selected pet type, configured service endpoints, and optional history-list mode.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

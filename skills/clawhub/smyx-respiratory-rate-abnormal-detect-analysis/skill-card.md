## Description:

Analyzes resting pet videos or video URLs to estimate respiratory rate, compare it with species and body-size baselines, and return abnormal-rate warnings, health-reference suggestions, report links, and history lookup output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, veterinary teams, and boarding-center staff use this skill to analyze resting pet videos for respiratory-rate warnings and structured report output. Results are health-reference support only and are not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags silent identity handling, uploads of pet videos or video URLs, and report-history access involving provider services.

Mitigation: Review before installing, use only when users are comfortable sharing those data with the provider, and make upload, account, privacy, and retention expectations explicit.

Risk: The security review flags active plaintext development endpoints and local token storage.

Mitigation: Use a release fixed to production HTTPS-only endpoints and protected token storage, or no token persistence, before normal deployment.

Risk: The security guidance flags a dependency issue around PyYAML.

Mitigation: Correct the PyYAML dependency before installation or packaging.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-respiratory-rate-abnormal-detect-analysis)
- [Respiratory Rate API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json]

**Output Format:** [Markdown text with structured JSON content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the same result to a user-specified output file.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence; artifact frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

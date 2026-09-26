## Description:

Analyzes reptile and arachnid pet image or video inputs through remote APIs to produce health findings, risk warnings, care suggestions, report links, and history lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze reptile or arachnid pet media, retrieve structured Pet Safety Guardian health reports, and list account-linked historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected pet media or supplied URLs to a remote service and can query account-linked report history.

Mitigation: Review the publisher's handling of token storage, account creation, and history-query controls before installing or using private media.

Risk: Security evidence reports active plaintext HTTP development endpoints despite HTTPS transport claims.

Mitigation: Do not use private media unless the publisher provides and documents a production HTTPS-only configuration.

Risk: Generated health findings may be incomplete or mistaken for veterinary diagnosis.

Mitigation: Treat reports as health reference material and consult a qualified veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [Crawl Analysis API Documentation](references/api_doc.md)
- [SMYX Analysis API Error Codes](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON health report text, with report links for history queries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis depends on remote API availability and supports local files or network URLs.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; artifact frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

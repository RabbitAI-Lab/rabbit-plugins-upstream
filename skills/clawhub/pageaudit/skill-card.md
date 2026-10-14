## Description:

Audits public pages for technical SEO issues, compares findings across releases, and suggests fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wrpbr](https://clawhub.ai/user/wrpbr)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site owners use PageAudit to inspect public pages for technical SEO problems, compare preview and production findings, and review suggested fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audited URLs and their fetched public HTML are sent to PageAudit; private links or sensitive query parameters could be disclosed.

Mitigation: Audit only public, non-sensitive URLs unless disclosure is acceptable; review the service terms and privacy policy first.

Risk: Audits do not execute page JavaScript and may miss content rendered only in the browser.

Mitigation: Verify browser-rendered content separately before relying on an audit for those pages.

## Reference(s):

- [PageAudit skill on ClawHub](https://clawhub.ai/wrpbr/skills/pageaudit)
- [PageAudit API reference](https://pageaudit.online/llms-full.txt)
- [PageAudit privacy policy](https://pageaudit.online/privacy)

## Skill Output:

**Output Type(s):** [Analysis, Code, Guidance]

**Output Format:** [Text or Markdown with findings, comparisons, and suggested patches]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include evidence and suggested fixes; preview comparisons identify regressions.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

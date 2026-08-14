## Description:

This skill analyzes cat, dog, or bird images and videos through cloud APIs to produce a Pet Safety Guardian health report with findings, warnings, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit pet media or media URLs for cloud-based health analysis and to retrieve prior Pet Safety Guardian reports. The results are health-reference guidance and are not a substitute for professional veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends pet media or media URLs to Life Emergence cloud services for analysis.

Mitigation: Review before installation and use only when the user accepts cloud processing of the submitted media.

Risk: Reports are tied to an automatically resolved local identity and history lookup can query cloud-stored reports.

Mitigation: Use an isolated workspace or account for testing and disclose that report history is associated with the resolved identity.

Risk: The security summary notes local storage of authentication tokens and profile data in a workspace SQLite database.

Mitigation: Limit workspace access, avoid sharing the workspace database, and remove local state after evaluation when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet health analysis API documentation](references/api_doc.md)
- [Analysis service API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands]

**Output Format:** [Markdown or JSON report text, optionally saved to a file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include health findings, risk warnings, care recommendations, report links, and history tables returned by cloud APIs.]

## Skill Version(s):

999.999.1004 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

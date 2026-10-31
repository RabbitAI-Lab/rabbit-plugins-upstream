## Description:

Analyzes indoor pet video for contact with hazardous non-food items and can issue a warning when contact lasts at least two seconds; it does not diagnose disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and smart-home monitoring users can submit indoor video to flag possible chewing or contact with hazardous non-food items and review a structured safety report. The report is for safety monitoring, not diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private household footage may be sent to a remote analysis service, and the export-only option may still make service calls.

Mitigation: Obtain explicit approval before remote analysis, use only footage intended for sharing, and confirm export-only mode stops all service calls.

Risk: The skill can silently create accounts and store credentials locally; its --api-url option may not change the configured service destination.

Mitigation: Provide clear account, credential-storage, and deletion controls; verify the configured destination directly and protect the workspace database.

Risk: Server retention practices and detection reliability are unverified.

Mitigation: Treat alerts as safety-monitoring guidance rather than diagnosis, and independently check the situation when an alert appears.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis report with risk alerts, suggestions, and report links; Markdown for report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Safety monitoring only; does not provide disease diagnosis.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata; packaged frontmatter says 1.0.22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

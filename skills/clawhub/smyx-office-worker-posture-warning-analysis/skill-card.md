## Description:

Analyzes office workstation video to estimate sitting duration and posture indicators, then returns prolonged-sitting and posture-warning reports without providing medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Workplace health, facilities, or developer teams use this skill to analyze office workstation videos or video URLs for prolonged sitting, forward-head posture, hunching, shoulder asymmetry, and screen-distance warnings. The output is intended for behavioral reminders and reporting, not medical diagnosis or treatment planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Office workstation video or video URLs may contain employee posture, activity, and workplace privacy data that is sent to an external service.

Mitigation: Require employee notice and consent before deployment, use approved video sources only, and review the service's retention, access control, and export policies.

Risk: The skill can silently create or reuse a user identity and store tokens locally for report access.

Mitigation: Protect the local data directory and token store, restrict who can run historical report queries, and rotate or delete tokens when access is no longer needed.

Risk: Historical reports and export links can expose workplace health-monitoring records.

Mitigation: Limit report-listing and export-link access to authorized users, audit access where possible, and avoid sharing report links outside approved channels.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-office-worker-posture-warning-analysis)
- [Publisher Profile](https://clawhub.ai/user/18072937735)
- [API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and JSON text with posture metrics, warning messages, historical report lists, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the rendered analysis text to a user-specified output file; historical report queries return structured report records from the configured cloud API.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

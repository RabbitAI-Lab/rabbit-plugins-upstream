## Description:

MacCheck runs a local Mac inspection, opens a guided hardware-check page, and helps users download inspection reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iluoyao](https://clawhub.ai/user/iluoyao)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill for routine Mac health checks, new or refurbished device acceptance, post-repair verification, pre-sale checks, and troubleshooting. It supports read-only system collection plus guided checks for hardware that requires user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inspection reports may include the Mac serial number and security status.

Mitigation: Review reports before sharing them and delete the output folder or browser saved state after use on shared machines.

Risk: The hardware-check page may request browser permissions for microphone, camera, USB, or file selection.

Mitigation: Grant only the permissions needed for the checks being performed and close the local page when the inspection is complete.

Risk: Some hardware and ownership signals require user confirmation or official Apple checks.

Mitigation: Treat results as local inspection evidence, not as an Apple official diagnostic, warranty decision, or purchase guarantee.

## Reference(s):

- [Server-resolved source repository](https://github.com/iluoyao/mac-check-skill)
- [ClawHub skill page](https://clawhub.ai/iluoyao/skills/mac-check-skill)
- [Architecture and Session Flow](references/architecture.md)
- [Privacy and Security](references/privacy.md)
- [Detection Catalog](references/detection-catalog.md)
- [Rule Specification](references/rule-spec.md)
- [Report Specification](references/report-spec.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, Files]

**Output Format:** [Agent guidance with local shell commands and downloadable Markdown, PDF, and PNG reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a local mac-check-output session folder and opens a self-contained local HTML inspection page.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 2.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

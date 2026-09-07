## Description:

A pre-install skill review helper that applies a four-phase source, code, permissions, and risk checklist, runs lightweight checks, and produces a vetting report for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill before installing or evaluating third-party skills to get a structured safety review, source check, and risk report. It supports installation decisions but leaves the final decision to a human reviewer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer and scanner behavior can affect local agent skill directories if broad or unintended paths are supplied.

Mitigation: Install only from a trusted, pinned release and use --agent or --dir deliberately.

Risk: Running checks against a broad home or project tree may include unrelated private files in the review scope.

Mitigation: Point the checker at the specific skill directory that needs review.

Risk: The source check contacts GitHub metadata for an explicitly named repository when network access is available.

Mitigation: Use source checks only for intended public repositories, or rely on the offline degradation path when network access is not appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-vetter)
- [Four-phase vetting checklist](references/checklist.md)
- [Vetting report template](references/vetting-report-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain text, JSON, and Markdown reports with occasional shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write a report file when requested; source checks degrade gracefully when network access is unavailable.]

## Skill Version(s):

0.2.4 (source: server release evidence; artifact files declare 0.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

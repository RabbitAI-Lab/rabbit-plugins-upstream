## Description:

Test the latest OpenClaw main commit through an isolated OCM copy or an explicitly approved in-place gateway update, then guide structured release feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openclaw](https://clawhub.ai/user/openclaw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release testers use this skill to validate an OpenClaw main build against a selected gateway, record manual surface testing, and prepare approved feedback for a shared release campaign.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify an OpenClaw gateway and use the tester's GitHub CLI session to dispatch workflows or publish approved reports.

Mitigation: Prefer the isolated OCM copy, require explicit approval before in-place updates, and review every proposed GitHub post before publication.

Risk: Release guidance is copied from a shared campaign issue into the private worksheet, so unexpected issue content can steer the validation run.

Mitigation: Require the expected label, hidden marker, current beta line, and campaign identity before preparing a gateway; stop if the campaign state is inconsistent.

Risk: In-place validation can update a real gateway, migrate state or plugins, and restart services.

Mitigation: Use the isolated path by default; for in-place mode, show the backup or snapshot and dry-run summary before accepting the exact approval phrase.

Risk: Validation reports can expose local paths, gateway names, logs, credentials, or user identifiers if drafts are not sanitized.

Mitigation: Use the structured report contract and privacy checks before publishing, and exclude local setup details, raw logs, credentials, and private identifiers from public comments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/openclaw/skills/release-validation)
- [OpenClaw publisher profile](https://clawhub.ai/user/openclaw)
- [Structured release report contract](references/structured-report.md)
- [Release validation worksheet](assets/validation-worksheet.md)
- [OpenClaw maturity scorecard](https://docs.openclaw.ai/maturity/scorecard.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON campaign artifacts, configuration snippets, worksheets, and reviewable GitHub post drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires human choices before gateway selection, in-place updates, diagnostics capture, and GitHub publication.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

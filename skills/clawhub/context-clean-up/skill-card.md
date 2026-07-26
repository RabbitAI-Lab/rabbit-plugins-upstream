## Description: <br>
Identifies prompt context bloat from session history, automation noise, and oversized bootstrap files, then produces an audit-only ranked cleanup plan with rollback notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phenomenoner](https://clawhub.ai/user/phenomenoner) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to diagnose bloated OpenClaw prompt context, identify top offenders, and plan low-risk cleanup steps without automatic deletion or unattended configuration edits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional audit report can include local session paths, message previews, or context details that may be sensitive. <br>
Mitigation: Treat generated JSON reports as private, review them before sharing, and redact sensitive details. <br>
Risk: Cleanup advice could remove useful context or reduce important automation visibility if applied without review. <br>
Mitigation: Apply only reviewed changes, keep backups or rollback steps, and verify behavior in a fresh session after changes. <br>
Risk: Out-of-band notification patterns can leak details if sent through channels the user does not control. <br>
Mitigation: Use only controlled delivery channels and keep notification payloads short or redacted. <br>


## Reference(s): <br>
- [Out-of-band delivery](references/out-of-band-delivery.md) <br>
- [Cron noise checklist](references/cron-noise-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON audit files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Audit-only; no automatic deletions or unattended configuration edits are performed.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

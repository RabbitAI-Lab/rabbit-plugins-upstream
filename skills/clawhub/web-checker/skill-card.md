## Description:

Audits web configuration and statically analyzes JavaScript bundles for exposed secrets, external endpoints, and potential XSS sinks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-hussein](https://clawhub.ai/user/z-hussein)

### License/Terms of Use:

MIT

## Use Case:

Developers and security engineers use it to review web configuration on domains they own or are authorized to assess, including headers, DNS, TLS, exposed paths and subdomains, and client-side JavaScript findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious due to report-writing overwrite and symlink concerns and installation requirement concerns; its review was incomplete for one source file.

Mitigation: Review report-writing behavior and the dependency range before installing. If proceeding, use a test environment and a report destination where overwriting an existing file would not cause harm.

## Reference(s):

- [OpenClaw documentation](https://docs.openclaw.ai/)
- [ClawHub web-checker release](https://clawhub.ai/z-hussein/skills/web-checker)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Terminal findings, JSON reports, or Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Severity-ranked findings include evidence and suggested actions; findings should be verified manually.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

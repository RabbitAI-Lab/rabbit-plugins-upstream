## Description:

Audit public software releases before installation using static artifacts, license checks, endpoint scans, and live distribution verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and security reviewers use this skill to audit unfamiliar public software releases before installation by comparing artifact metadata, licenses, endpoints, and live distribution links without executing installers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Static inspection cannot exclude dynamic network behavior or installer side effects.

Mitigation: Keep downloads in a temporary isolated workspace, inspect unpacked files as data, and treat any later installation or execution as a separate decision.

Risk: Advertised installers or manifests may redirect to missing or different release assets.

Mitigation: Follow redirects and record the final HTTP status before relying on a distribution claim.

Risk: Source, packaged engine, desktop assets, and templates may carry different licenses or rights.

Mitigation: Compare embedded artifact licenses and metadata with repository and template licenses, then report rights per component.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/preinstall-release-audit)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with cited findings and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static preinstallation audit; installation or execution remains a separate decision.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

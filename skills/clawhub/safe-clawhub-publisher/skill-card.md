## Description:

Safely validate, dry-run, publish, and verify ClawHub skills and OpenClaw plugins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geoffrey-xiao](https://clawhub.ai/user/geoffrey-xiao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release maintainers use this skill to prepare ClawHub skill and OpenClaw plugin releases by validating package contents, dry-running publication, checking authentication and ownership, and verifying post-release state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Release publication, login, installation, tag changes, and remote replacement can mutate local or remote state.

Mitigation: The workflow gates high-impact actions behind dry-runs, evidence checks, pre-publication integrity checks, and explicit confirmation for the displayed account, target, version, command, file set, and fingerprint.

Risk: Credentials or tokens could be exposed during authentication or release review.

Mitigation: The skill directs agents to use supported CLI authentication flows or masked CI secrets, avoid printing stored tokens, and show only short-lived device-flow details when needed.

Risk: A package could be published with the wrong owner, slug, version, or file set.

Mitigation: The workflow requires resolving the remote package, comparing validator and CLI dry-run fingerprints, checking the authenticated account, and aborting when any confirmed value changes.

Risk: An unclear publish response could lead to duplicate publication attempts.

Mitigation: The troubleshooting guidance limits follow-up to bounded non-mutating inspections and requires authoritative failure evidence plus fresh confirmation before any retry.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/geoffrey-xiao/skills/safe-clawhub-publisher)
- [Skill release](references/skill-release.md)
- [Plugin package release](references/plugin-release.md)
- [Release security checklist](references/security-checklist.md)
- [Version and changelog decisions](references/versioning.md)
- [Troubleshooting](references/troubleshooting.md)
- [ClawHub release report](assets/release-report.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and release report templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include validation summaries, file hashes, fingerprints, release plans, changelog recommendations, and exact publish commands without secret values.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

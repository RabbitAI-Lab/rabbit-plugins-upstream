## Description:

Accidental ClawHub publish or leaked package files: scope, remove, and verify one affected version.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to respond to accidental ClawHub publication incidents by scoping the affected version, separating registry exposure from Git exposure, removing the exact affected version with approval, and verifying registry state afterward.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exact-version deletion is irreversible and may remove a version that is still needed.

Mitigation: Require explicit user approval, target only one exact version, and publish a corrected replacement before deleting the current latest version.

Risk: Registry exposure may be confused with Git exposure, local cache state, or conversation and log exposure.

Mitigation: Report registry, Git, local cache, and conversation/log exposure as separate findings, and escalate credentials, personal data, or private communications beyond package deletion.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces an incident-response checklist and verification steps; it does not execute deletion without explicit user approval.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

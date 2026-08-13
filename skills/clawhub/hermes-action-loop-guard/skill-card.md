## Description:

Adds pytest-free deterministic verification for tool progress guard installs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators administering Hermes instances use this skill to diagnose action-promise stalls and tool-call loops, then apply bounded guardrail installers with status checks, dry runs, backups, verification, and rollback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled installers make live changes to Hermes source and configuration and may briefly restart the gateway service.

Mitigation: Use only on a Hermes instance you administer, run status and dry-run first, keep the printed backup path, and verify the gateway reconnects after installation.

Risk: Rollback reads a backup manifest and can execute unsafe operations if pointed at an untrusted backup directory.

Mitigation: Run rollback only with the exact backup path created by the installer and do not use backup directories you did not create and trust.

Risk: Unsupported or ambiguous Hermes layouts can cause unsafe patching decisions.

Mitigation: Treat compatibility failures as fail-closed and rerun status, compatibility tests, and dry-run after Hermes upgrades before reinstalling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/hermes-action-loop-guard)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and installer output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational instructions for a Hermes administrator and uses bundled installers that modify live Hermes source and configuration when executed.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Installs bounded Hermes guards that detect action stops and tool-call loops, redirect repeated loop stops, and preserve rollback and gateway lifecycle state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators maintaining Hermes hosts use this skill to assess action-stop and tool-call loop symptoms, run dry-run compatibility checks, install the appropriate guard, verify gateway recovery, and roll back from controlled backups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installers persistently patch Hermes agent runtime files and configuration.

Mitigation: Run status, compatibility tests, and install --dry-run before installation, and stop if any source anchor is missing or ambiguous.

Risk: Gateway availability can be affected because installation and rollback stop and restart the Hermes gateway.

Mitigation: Plan the patch window, verify the gateway state after changes, and confirm the messaging WebSocket reconnects.

Risk: Rollback can be unsafe if performed from an untrusted or uncontrolled backup directory.

Mitigation: Use only the exact backup path printed by the installer, inspect the backup manifest, and avoid rollback from backup directories you did not create and control.

Risk: The skill changes core agent behavior by adding bounded recovery for action stops and tool-loop redirects.

Mitigation: Validate the provided fixtures and keep the documented redirect and hard-stop bounds in place before using it on a live Hermes host.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/hermes-action-loop-guard)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and operational checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include status, dry-run, install, verify, rollback, and compatibility-test commands for a Hermes host.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

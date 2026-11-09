## Description:

Offline, read-only scans of OpenClaw, Hermes Agent, nanobot, PicoClaw, ZeroClaw, NanoClaw, or other agent folders report per-message context size, scheduled-task and heartbeat costs, plaintext secrets, and suspicious or bloated memory without network access or added dependencies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyseal](https://clawhub.ai/user/psyseal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent owners use this skill to review local AI agent files for context-loading issues, scheduled-task and heartbeat costs, exposed secrets, and suspicious or oversized memory, then inspect the report's suggested fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Symlink exclusion is incomplete, so scanning configuration or workspace paths may reach files outside the intended scope.

Mitigation: Verify that the selected paths and their parent directories are trusted; narrow the audit with --path or --platform.

Risk: Reports include local paths and diagnostic metadata that may be sensitive when shared.

Mitigation: Review reports before sharing them.

## Reference(s):

- [Server-resolved source repository](https://github.com/psyseal/psyseal-scan)
- [Full scanner source](https://github.com/psyseal/scanner)
- [ClawHub skill page](https://clawhub.ai/psyseal/skills/psyseal-scan)
- [Psyseal](https://psyseal.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable scan report or JSON report with findings and suggested fixes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Secret values and memory text are omitted; cost figures may be estimates.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

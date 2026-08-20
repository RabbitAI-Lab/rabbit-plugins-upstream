## Description:

Provides a standardized MT5/Vantage EA deployment runbook for copying, compiling, restarting, attaching, and verifying the DRT-Axe expert advisor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohamedabdisamed](https://clawhub.ai/user/mohamedabdisamed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to deploy and verify changes to the DRT-Axe EA in a controlled MT5/Vantage trading environment. It helps standardize repeatable deployment steps and common troubleshooting checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to overwrite trading automation files and restart MT5, which may affect live trading behavior.

Mitigation: Use only in a controlled MT5/Vantage environment with manual approval, backups of replaced EA files, active-order checks, a maintenance window, and rollback steps.

Risk: Compilation, attach, or dialog handling failures could leave the EA stopped or running an unexpected version.

Mitigation: Review diffs before deployment and verify runtime using compile results, fresh heartbeat files, current log entries, and service-state checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mohamedabdisamed/skills/ea-upload-opsaetning)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks and verification tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational paths, expected log signals, troubleshooting steps, and reporting guidance.]

## Skill Version(s):

1.0.0 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

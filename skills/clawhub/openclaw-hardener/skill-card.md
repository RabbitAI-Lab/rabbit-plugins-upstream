## Description: <br>
Harden OpenClaw workspaces and ~/.openclaw data by running security audits, workspace hygiene checks, secret-aware scans, safe opt-in fixes, and optional config.patch planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[virtaava](https://clawhub.ai/user/virtaava) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to review and harden an OpenClaw installation before or during normal use. It supports read-only checks by default, with explicit opt-in modes for mechanical fixes and gateway configuration changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has broad local read/write and subprocess authority over the repository and ~/.openclaw data. <br>
Mitigation: Run check mode first in a clean working tree and review findings before using fix or apply-config modes. <br>
Risk: Fix and apply-config modes can mutate local files or gateway configuration. <br>
Mitigation: Use plan-config to inspect proposed configuration changes and apply them only after confirming the exact patch. <br>
Risk: The skill inspects sensitive local paths and command output while performing security checks. <br>
Mitigation: Keep output private, confirm redaction before sharing results, and avoid sharing raw logs that may contain local paths or sensitive context. <br>


## Reference(s): <br>
- [OpenClaw Hardener on ClawHub](https://clawhub.ai/virtaava/skills/openclaw-hardener) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Plain text or JSON findings, command examples, and optional JSON config.patch plans] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended to redact likely secrets; fix and apply-config modes can change local files or gateway configuration only when explicitly invoked.] <br>

## Skill Version(s): <br>
0.1.2 (source: openclaw-skill.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

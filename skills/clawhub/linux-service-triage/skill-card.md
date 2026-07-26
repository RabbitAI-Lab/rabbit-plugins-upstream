## Description: <br>
Diagnoses common Linux service issues using logs, systemd/PM2, file permissions, Nginx reverse proxy checks, and DNS sanity checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kowl64](https://clawhub.ai/user/kowl64) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to triage Linux services that are failing, unreachable, or misconfigured. It turns supplied status output, logs, service names, paths, Nginx snippets, domains, and ports into a likely cause, minimal fix plan, verification steps, and optional safe commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Proposed reloads, permission changes, or service definitions can affect service availability or persistence. <br>
Mitigation: Review every proposed command before running it on a real server, keep changes explicit and scoped, and prefer reversible steps. <br>
Risk: Troubleshooting output can lead to incorrect fixes when logs, status output, service names, paths, ports, or Nginx configuration are missing or stale. <br>
Mitigation: Use current user-supplied evidence, confirm scope before privileged actions, test Nginx configuration before reloads, and verify health after changes. <br>


## Reference(s): <br>
- [Linux Service Triage Commands](references/triage-commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown triage report with optional shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are provided only when the user explicitly approves changes and the action is safe.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

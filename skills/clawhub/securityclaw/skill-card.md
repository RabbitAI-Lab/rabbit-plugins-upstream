## Description: <br>
SecurityClaw audits OpenClaw skills for prompt-injection, exfiltration, supply-chain, and unsafe-tooling risks, supports optional quarantine, and produces owner-action guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mallen-lbx](https://clawhub.ai/user/mallen-lbx) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use SecurityClaw to scan OpenClaw skill directories for risky patterns, review JSON findings, and decide whether to quarantine, delete, report, allow, or rescan flagged skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Quarantine mode can move flagged skill folders out of the active OpenClaw skills directory. <br>
Mitigation: Run the default read-only scan first, review the report, and use --quarantine only when comfortable with moving flagged folders. <br>
Risk: The scanner uses risk indicators that can flag legitimate skills for command execution, network access, sensitive paths, install hooks, or prompt-injection markers. <br>
Mitigation: Review file and line findings before acting, use allowlists and contextual checks, and avoid executing high-severity skills until reviewed. <br>
Risk: Dynamic checks of untrusted skills can expose secrets, writable configuration, network access, or privileged tools if run without isolation. <br>
Mitigation: Run dynamic checks only after owner approval in an OS-level sandbox with no network egress, read-only filesystem access except a temporary workspace, and no access to OpenClaw secrets. <br>


## Reference(s): <br>
- [SecurityClaw ClawHub skill page](https://clawhub.ai/mallen-lbx/skills/securityclaw) <br>
- [SecurityClaw rule catalog](references/rules.md) <br>
- [Sandboxing strategy](references/sandboxing.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON scan reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The scanner is read-only by default and writes a JSON report; quarantine mode can move high-severity skill folders to a quarantine directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

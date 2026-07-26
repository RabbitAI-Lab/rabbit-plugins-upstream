## Description: <br>
Diagnose Linux OS-level issues including slow servers, OOM kills, disk fullness, high CPU or load, DNS failures, connection timeouts, port exhaustion, file descriptor limits, zombie processes, browser automation failures, locale problems, and kernel misconfigurations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zjxylc](https://clawhub.ai/user/zjxylc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and site reliability engineers use this skill to guide Linux server diagnostics and produce severity-sorted findings with observed values and remediation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports that a DNS nameserver reachability check can turn malformed resolver data into root-run shell code. <br>
Mitigation: Review the shell script before root execution and fix or skip the nameserver reachability line. <br>
Risk: Diagnostic output can include process names, socket owners, kernel messages, configuration details, and selected log lines. <br>
Mitigation: Treat generated output as sensitive, run only relevant sections where possible, and restrict sharing to authorized reviewers. <br>
Risk: The workflow is intended for Linux diagnostics and commonly requires root or sudo access to collect full system signals. <br>
Mitigation: Install and run it only when Linux server diagnostics are needed, and review commands before executing privileged sections. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zjxylc/skills/linux-system-health) <br>
- [Project homepage](https://github.com/ecsgo-helper/openclaw-system-health) <br>
- [Issue registry and severity reference](artifact/reference.md) <br>
- [Artifact README](artifact/README.md) <br>
- [Diagnostic script](artifact/scripts/diagnostics.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell command blocks and severity-sorted diagnostic findings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings are expected to include issue name, severity, observed value versus threshold, and recommended remediation.] <br>

## Skill Version(s): <br>
1.2.1 (source: ClawHub release metadata; artifact frontmatter lists 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

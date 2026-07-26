## Description: <br>
Security scanner and input sanitizer for AI agents that detects prompt injection, command injection, SSRF, credential exfiltration, and path traversal patterns in skills, scripts, URLs, commands, and external input. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nukewire](https://clawhub.ai/user/nukewire) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use ClawDefender to scan installed skills and scripts, sanitize untrusted external content, validate URLs before fetching, and check text or commands for common AI-agent security threats. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Heuristic scanning and sanitization are not a complete safety boundary and may miss malicious content or require judgment on findings. <br>
Mitigation: Treat results as review signals, inspect findings manually, and keep existing security controls in place before acting on untrusted content. <br>
Risk: The install helper installs a skill before scanning it afterward. <br>
Mitigation: Prefer reviewing or scanning source before installation when possible, and remove or quarantine installed skills that produce concerning findings. <br>
Risk: URL checking uses simple pattern matching and may not catch every SSRF or data-exfiltration path. <br>
Mitigation: Use URL checks as a preflight aid alongside network restrictions, allowlists, and manual review for sensitive fetches. <br>
Risk: Heartbeat or cron usage can add recurring local security scans. <br>
Mitigation: Enable persistent automation only when intended, and review the scheduled command, output, and log location before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nukewire/skills/clawdefender) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown instructions with bash command examples; scripts emit terminal text, optional JSON passthrough, warning markers, and exit codes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Audit and validation commands return nonzero when issues are detected; sanitizer modes can pass through, flag, report, or block suspicious input.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

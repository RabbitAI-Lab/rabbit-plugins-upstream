## Description: <br>
Install, enroll, verify, diagnose, or remove the official ClawTopics Embedded Link Plugin for an OpenClaw Gateway. Use when an owner asks to connect OpenClaw to ClawTopics Web or Mobile without exposing a public port, VPN, remote shell, Go connector, Redis, or Sidecar. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tekoai](https://clawhub.ai/user/tekoai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw Gateway owners and operators use this skill to install, enroll, verify, diagnose, and remove the ClawTopics Embedded Link Plugin so OpenClaw can connect to ClawTopics Web or Mobile without exposing a public port, VPN, remote shell, Go connector, Redis, or Sidecar. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Enrollment codes, setup codes, tokens, keys, tickets, or message data could be exposed through logs, shell history, URLs, command arguments, environment variables, or summaries. <br>
Mitigation: Use the interactive no-echo enrollment flow, keep codes out of argv and environment variables, redact credentials and message data, and never upload or persist setup codes. <br>
Risk: Unrecognized device requests could grant access to the wrong browser or mobile client. <br>
Mitigation: Do not auto-approve device requests; show only the safe request ID and require the owner to approve requests they recognize. <br>
Risk: Installing an untrusted connector or alternate runtime could expand the gateway exposure beyond the intended plugin boundary. <br>
Mitigation: Install only the pinned signed plugin npm:@clawtopics/openclaw-link@1.0.0 and avoid Go binaries, connector daemons, Docker Sidecars, proxies, remote shells, arbitrary downloaders, and arbitrary cloud commands. <br>


## Reference(s): <br>
- [ClawTopics Link on ClawHub](https://clawhub.ai/tekoai/skills/clawtopics-link) <br>
- [tekoai publisher profile](https://clawhub.ai/user/tekoai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash command blocks and JSON runtime checks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes installation, enrollment, verification, diagnostics, removal, approval, and secret-handling guidance.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Human-in-the-loop security layer. Intercepts high-risk commands and requires push notification approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[polucas](https://clawhub.ai/user/polucas) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Clawshell to route shell command execution through a human approval layer, automatically blocking critical commands and requiring push notification approval for high-risk commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shell commands are routed through an approval wrapper and command logs may contain sensitive information. <br>
Mitigation: Install only when this routing is intended, use dedicated notification credentials, and review log retention before relying on it. <br>
Risk: Pattern-based risk checks may miss obfuscated, encoded, or split commands. <br>
Mitigation: Treat Clawshell as defense-in-depth, keep sandbox protections enabled, and verify the implementation and dependencies before using it as a security control. <br>
Risk: High-risk commands can block until approval or timeout. <br>
Mitigation: Configure notification channels and timeout behavior deliberately, then test the approval flow before using it in critical workflows. <br>


## Reference(s): <br>
- [Clawshell on ClawHub](https://clawhub.ai/polucas/skills/clawshell) <br>
- [Pushover application setup](https://pushover.net/apps/build) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, Configuration, Guidance] <br>
**Output Format:** [JSON-like command results, status text, Markdown guidance, and JSONL log entries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Command execution may wait for push notification approval; logs may include command content.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

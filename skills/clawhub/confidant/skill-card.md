## Description: <br>
Confidant provides a secure secret handoff and credential setup wizard for AI agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ericsantos](https://clawhub.ai/user/ericsantos) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Confidant to request API keys, passwords, and tokens through a browser handoff, then save credentials to configured files without exposing secrets in chat. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confidant handles credentials through local tooling and can expose a request through an optional public tunnel. <br>
Mitigation: Use scoped and revocable secrets, prefer local-only handoff when possible, and stop any tmux, server, or tunnel processes after the handoff. <br>
Risk: Credentials may be saved to broad or arbitrary paths, or printed when stdout mode is used. <br>
Mitigation: Avoid stdout mode for sensitive secrets, verify every save path before sharing the link, and prefer conventional service-specific credential files. <br>
Risk: The workflow depends on local npm packages and command-line tooling that must be trusted by the operator. <br>
Mitigation: Install only when the @aiconnect/confidant and localtunnel packages are acceptable for the environment, and review required binaries before use. <br>


## Reference(s): <br>
- [Confidant on ClawHub](https://clawhub.ai/ericsantos/skills/confidant) <br>
- [Publisher profile](https://clawhub.ai/user/ericsantos) <br>
- [Confidant homepage declared in skill metadata](https://github.com/aiconnect-cloud/confidant) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce a shareable secret-submission URL and save received credentials to local configuration files.] <br>

## Skill Version(s): <br>
1.5.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

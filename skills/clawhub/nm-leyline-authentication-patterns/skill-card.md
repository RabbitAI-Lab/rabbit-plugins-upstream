## Description: <br>
Provides auth patterns for API keys, OAuth, and token management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when implementing or reviewing external service authentication, credential verification, token handling, and authentication failure recovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authentication examples may handle API keys, OAuth tokens, and service credentials. <br>
Mitigation: Do not commit `.env` or token files; prefer provider CLIs or secret stores with tight file permissions for real credentials. <br>
Risk: Shell and CLI examples can perform authenticated operations when adapted into a workflow. <br>
Mitigation: Review commands before running them and avoid untrusted service names or credential inputs. <br>


## Reference(s): <br>
- [Leyline homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-authentication-patterns) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with Python, Bash, and YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; review commands before running them and protect credentials carefully.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

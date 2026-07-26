## Description: <br>
Circle connector skill for reading, creating, and updating Circle data through an OOMOL-connected account using the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect Circle connector schemas and run Circle community, member, post, space group, and space member actions through the oo CLI with OOMOL-managed credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can access connected Circle account data and may run actions that affect Circle content. <br>
Mitigation: Install only when Circle access through OOMOL is intended, inspect the live action schema before payload construction, and confirm write or destructive payloads with the user before execution. <br>
Risk: Setup commands can trigger unnecessary CLI installation, login, connection, or billing flows if run proactively. <br>
Mitigation: Use first-time setup steps only after an oo command, authentication, connection, scope, or billing error indicates they are needed. <br>


## Reference(s): <br>
- [Circle homepage](https://circle.so) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples; connector responses are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill instructs the agent to inspect the live connector schema before building action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

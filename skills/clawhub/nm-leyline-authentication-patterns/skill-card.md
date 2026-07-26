## Description: <br>
Provides auth patterns for API keys, OAuth, and token management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when implementing or reviewing authentication flows for external services, including API keys, OAuth, token management, credential verification, and auth failure handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authentication examples may be copied into production without adapting credential handling to the target service and environment. <br>
Mitigation: Treat the examples as guidance, review token storage and error handling, and validate the final flow against the service's supported CLI or API. <br>
Risk: Examples using service names could lead an agent to run unintended commands if names are arbitrary or user-supplied. <br>
Mitigation: Restrict command examples to known CLIs such as gh, glab, aws, gcloud, and az, and review commands before execution. <br>
Risk: Token caching and CI secret handling can expose credentials on shared machines or runners. <br>
Mitigation: Review cache locations, permissions, TTLs, and CI environment variables before use in shared environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-authentication-patterns) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [Authentication methods module](modules/auth-methods.md) <br>
- [Interactive authentication module](modules/interactive-auth.md) <br>
- [Verification patterns module](modules/verification-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python, shell, and YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only authentication guidance; review examples before adapting them to production systems.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

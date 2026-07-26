## Description: <br>
Gowok helps agents guide Go developers through using the Gowok library to build project starters, REST APIs, gRPC services, event workers, configuration, web routing, SQL access, singleton containers, and nil-safe helpers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hadihammurabi](https://clawhub.ai/user/hadihammurabi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill for guidance on starting and configuring Go services with Gowok, including HTTP servers, gRPC or net listeners, workers, SQL connections, singleton state, and nil-safe value handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Go dependency and database driver commands may affect a real project dependency graph. <br>
Mitigation: Review Go dependency and driver installation commands before applying them to production repositories. <br>
Risk: Server, pprof, CORS, and SQL configuration examples can expose services, profiling endpoints, or databases if copied without environment-specific review. <br>
Mitigation: Review listener addresses, pprof exposure, CORS settings, secrets, and SQL DSNs before using the examples in deployed services. <br>


## Reference(s): <br>
- [Gowok on ClawHub](https://clawhub.ai/hadihammurabi/skills/gowok) <br>
- [Getting Started](references/getting-started.md) <br>
- [Configuration](references/configuration.md) <br>
- [Runner](references/runner.md) <br>
- [Singleton](references/singleton.md) <br>
- [Web](references/web.md) <br>
- [Some (Nil Safety)](references/some.md) <br>
- [SQL](references/sql.md) <br>
- [Go](https://go.dev) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Go, YAML, bash, and HTTP examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

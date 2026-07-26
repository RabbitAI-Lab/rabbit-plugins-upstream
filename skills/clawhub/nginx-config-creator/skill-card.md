## Description: <br>
Creates a standard Nginx/OpenResty reverse proxy config file for a service and reloads the web server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xieyuanqing](https://clawhub.ai/user/xieyuanqing) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to generate and apply Nginx/OpenResty reverse proxy configuration for services behind a Dockerized web server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can write, overwrite, or delete Nginx configuration files in the configured conf.d directory. <br>
Mitigation: Use a known-safe config directory, review the generated file path before execution, and back up existing configuration before applying changes. <br>
Risk: Reloading the specified Dockerized Nginx/OpenResty container can affect live traffic if the wrong container or configuration is targeted. <br>
Mitigation: Confirm the container name, service name, domain, and port before running the command, and rely on the included nginx -t check before reload. <br>
Risk: Untrusted values for service name, domain, port, config path, or container name can lead to unintended configuration changes. <br>
Mitigation: Accept these values only from trusted operators or validated deployment metadata. <br>


## Reference(s): <br>
- [Nginx Config Creator on ClawHub](https://clawhub.ai/xieyuanqing/skills/nginx-config-creator) <br>
- [xieyuanqing ClawHub publisher profile](https://clawhub.ai/user/xieyuanqing) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with bash command examples and generated Nginx configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash and docker; writes an Nginx conf.d file, tests the configuration, reloads Nginx on success, and removes the generated file on test or reload failure.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Automatically detects a project type, generates a Dockerfile when needed, builds the application image, and deploys it with Docker using port selection and health checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bustes01](https://clawhub.ai/user/bustes01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to turn local projects, archives, or repository checkouts into Docker-based deployments with generated Dockerfiles, build commands, container startup, status, log, and stop workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Docker installation workflow can make privileged host changes. <br>
Mitigation: Review or manually run the Docker installation step, and only use it on hosts where agent-managed Docker setup is acceptable. <br>
Risk: Generated Dockerfiles may build and run projects with incorrect assumptions. <br>
Mitigation: Inspect generated Dockerfiles before building and deploying containers. <br>
Risk: Stop and deploy commands can remove containers by name without verifying a managed label first. <br>
Mitigation: Avoid using stop or redeploy commands on hosts with important unrelated containers until the workflow verifies deploy-agent labels before removal. <br>


## Reference(s): <br>
- [Deploy Agent on ClawHub](https://clawhub.ai/bustes01/skills/deploy-agent) <br>
- [Publisher profile](https://clawhub.ai/user/bustes01) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated Docker configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write Dockerfiles into project directories and run Docker commands on the host when the user invokes deployment workflows.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

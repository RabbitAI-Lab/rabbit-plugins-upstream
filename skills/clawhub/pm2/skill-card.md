## Description: <br>
Manage Node.js applications with PM2 process manager. Use for deploying, monitoring, and auto-restarting Node apps in production. Covers starting apps, viewing logs, setting up auto-start on boot, and managing multiple processes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asteinberger](https://clawhub.ai/user/asteinberger) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to manage Node.js applications with PM2, including deployment, monitoring, restarts, startup persistence, logs, and ecosystem configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Process-control commands can stop or remove PM2-managed services. <br>
Mitigation: Review target process names and avoid stop, delete, kill, or delete-all commands unless service interruption is intended. <br>
Risk: Startup persistence commands may change boot behavior and require elevated privileges. <br>
Mitigation: Run pm2 startup and sudo startup commands only when automatic restart after reboot is desired and the generated command has been reviewed. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash and JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides command examples and configuration snippets for PM2-managed Node.js applications.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

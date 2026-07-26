## Description: <br>
Build, edit, and deploy Instant-backed apps using npx instant-cli, create-instant-app (Next.js + Codex), GitHub (gh), and Vercel (vercel). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stopachka](https://clawhub.ai/user/stopachka) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to create, modify, version, and deploy Instant-backed Next.js applications under a local apps workspace. It guides agents through GitHub repository setup, Vercel production deployment, and environment variable handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad authority to create repositories, push to main, deploy to production, and manage app environment variables. <br>
Mitigation: Confirm the app folder, repository, branch, and Vercel project before execution; review commits and deployment targets before allowing push or production deploy steps. <br>
Risk: The skill instructs the agent to push local .env values to Vercel when deployment variables are missing. <br>
Mitigation: Review each environment variable key and value before upload, exclude secrets that should remain local, and prefer least-privilege deployment tokens. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Markdown] <br>
**Output Format:** [Markdown guidance with shell commands, code edits, configuration changes, and deployment status updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or modify app files, Git commits, GitHub repositories, Vercel deployments, and environment variable configuration when used with authenticated tools.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

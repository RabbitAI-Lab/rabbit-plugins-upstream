## Description: <br>
Guide Claude through deploying serverless browser automation using the official bb CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[peytoncasper](https://clawhub.ai/user/peytoncasper) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation engineers use this skill to create, test, deploy, and invoke Browserbase Functions for scheduled, webhook, or cloud browser automation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browserbase API keys, project IDs, and login credentials are required for the workflows described by the skill. <br>
Mitigation: Keep Browserbase and login credentials out of git, avoid hardcoding real account passwords, and use test or least-privilege accounts for remote browser automation. <br>
Risk: The skill proposes pnpm and bb CLI commands that initialize, run, publish, and invoke remote browser automation. <br>
Mitigation: Review commands before running them and install only when you intend to use Browserbase Functions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/peytoncasper/skills/functions) <br>
- [Browserbase settings](https://browserbase.com/settings) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with shell, TypeScript, JSON, and environment-variable examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include Browserbase API calls, bb CLI commands, .env setup, and code patterns for deployment and invocation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

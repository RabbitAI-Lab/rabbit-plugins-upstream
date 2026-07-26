## Description: <br>
Wundervault Vault helps agents read passwords, API keys, and credentials from a Wundervault zero-knowledge, multi-agent vault and run authorized shell commands with secrets injected without exposing plaintext in chat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[snoweman](https://clawhub.ai/user/snoweman) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let agents access scoped vault entries, run commands with injected secrets, write approved environment-file entries, and perform SSH or rsync workflows without exposing plaintext credentials in chat. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup URLs and generated credential files can grant agent access if mishandled. <br>
Mitigation: Treat setup URLs and generated credential files as secrets, and verify the npm package plus onboarding script checksums before use. <br>
Risk: Injected secrets can enable high-impact commands, deployments, publishing, or wallet-signing actions. <br>
Mitigation: Grant each agent only the vault entries it needs, keep high-impact keys at an approval tier, and review approval requests before retrying denied actions. <br>
Risk: Environment-file injection can persist secrets on disk in paths the agent can reach. <br>
Mitigation: Enable environment-file injection only for projects where persistent on-disk secrets are acceptable, review target paths, and manage file permissions outside the skill. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/snoweman/skills/wundervault-vault) <br>
- [Wundervault install checksums](https://wundervault.com/install) <br>
- [Wundervault verification guide](https://wundervault.com/verify) <br>
- [Wundervault agent wallets](https://wundervault.com/agent-wallets) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline tool-call examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can guide vault MCP tool use for listing entries, injecting secrets into approved command environments, writing environment files, and syncing files over SSH.] <br>

## Skill Version(s): <br>
1.6.9 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

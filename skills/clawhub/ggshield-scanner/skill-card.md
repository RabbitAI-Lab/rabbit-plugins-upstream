## Description: <br>
Detect 500+ types of hardcoded secrets (API keys, credentials, tokens) before they leak into git. Wraps GitGuardian's ggshield CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amascia-gg](https://clawhub.ai/user/amascia-gg) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to ask an agent to scan repositories, individual files, staged git changes, and Docker images for hardcoded secrets before code is committed or released. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scanning code may send information to GitGuardian, and the artifact's privacy claims may understate that data sharing. <br>
Mitigation: Use the skill only for code that may be scanned under the user's policy, and use an approved GitGuardian endpoint when required. <br>
Risk: The skill requires a GitGuardian API key for scanning. <br>
Mitigation: Use a revocable API key with appropriate scope and rotate or revoke it if exposed. <br>
Risk: The skill executes the external ggshield CLI and depends on the installed package source. <br>
Mitigation: Verify the ggshield binary and package source before installing or running the skill. <br>
Risk: The install-hooks command can modify local git hook behavior. <br>
Mitigation: Require explicit user approval before installing pre-commit or pre-push hooks. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/amascia-gg/skills/ggshield-scanner) <br>
- [ggshield documentation](https://docs.gitguardian.com/ggshield-docs/) <br>
- [GitGuardian dashboard](https://dashboard.gitguardian.com) <br>
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text or Markdown-style status messages with ggshield scan results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the ggshield binary and GITGUARDIAN_API_KEY; can scan repositories, files, staged changes, and Docker images.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact pyproject.toml reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

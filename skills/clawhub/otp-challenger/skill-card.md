## Description: <br>
Enables agents and skills to challenge users for fresh two-factor authentication proof (TOTP or YubiKey) before sensitive actions such as deployments, financial operations, data access, admin operations, and change control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ryancnelson](https://clawhub.ai/user/ryancnelson) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to require fresh TOTP or YubiKey proof before an agent proceeds with sensitive approval workflows. It is suited for deployment gates, financial approvals, protected data access, admin changes, and change-control checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can locally use or generate OTP codes, and the same agent may be able to read the secret or run a current-code helper. <br>
Mitigation: Use it as a workflow approval check rather than independent MFA; store OTP and YubiKey secrets in a secret manager or tightly permissioned config and restrict helper access. <br>
Risk: OTP_FAILURE_HOOK can execute arbitrary shell commands when verification fails. <br>
Mitigation: Leave OTP_FAILURE_HOOK unset unless it points to a trusted fixed script reviewed for least privilege. <br>
Risk: YubiKey verification depends on outbound HTTPS access to Yubico. <br>
Mitigation: Allow only the required Yubico HTTPS path and fail closed when network verification is unavailable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ryancnelson/skills/otp-challenger) <br>
- [Project homepage](https://github.com/ryancnelson/otp-challenger) <br>
- [Yubico OTP documentation](https://developers.yubico.com/OTP/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and plain-text verification status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Verification scripts return exit codes for success, invalid or rate-limited codes, and configuration errors.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

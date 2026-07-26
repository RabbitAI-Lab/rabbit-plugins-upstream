## Description: <br>
Helps agents purchase and apply Alibaba Cloud CAS SSL certificates across China and International sites, including certificate instance acquisition, reuse, and DV/OV/EV application flows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to guide Alibaba Cloud SSL certificate purchasing, instance reuse, application submission, and status verification through CAS and BSS CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide paid Alibaba Cloud certificate instance purchases. <br>
Mitigation: Confirm the profile, region, domain, certificate authority, duration, and expected cost before approving any purchase or application step. <br>
Risk: Cloud credentials can be exposed if AccessKey secrets are pasted into chat, commands, logs, or shell history. <br>
Mitigation: Use preconfigured CLI profiles or OAuth where possible, and do not place AccessKey secrets in the conversation or logged command lines. <br>
Risk: Remote CLI installer commands can execute code from a downloaded script. <br>
Mitigation: Prefer trusted package manager or manual installation paths when appropriate, and avoid piping remote installers directly to a shell. <br>
Risk: Retrying non-idempotent purchase commands after a timeout can create duplicate charges. <br>
Mitigation: Check order status before retrying purchase commands and proceed only after user-driven confirmation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-cas-ssl-cert-purchase) <br>
- [API Commands](references/api-commands.md) <br>
- [RAM Policies](references/ram-policies.md) <br>
- [Related CLI Commands](references/related-commands.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Error Handling](references/error-handling.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown] <br>
**Output Format:** [Markdown with inline shell commands and parameter tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Alibaba Cloud CLI commands, environment variable exports, confirmation prompts, and status-verification steps.] <br>

## Skill Version(s): <br>
0.0.1-beta.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

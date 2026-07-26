## Description: <br>
Manage a put.io account via the kaput CLI for transfers, files, search, and transfer status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baanish](https://clawhub.ai/user/baanish) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to manage put.io transfers and files from an agent-assisted shell workflow using the kaput CLI. It helps add magnet or URL transfers, check authentication, list transfers, search files, and view transfer status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses the unofficial kaput CLI with a user's put.io account. <br>
Mitigation: Install only if comfortable with that CLI and use the documented device-code login flow. <br>
Risk: Account tokens and local kaput configuration are sensitive. <br>
Mitigation: Do not paste credentials or tokens into chat, and avoid sharing kaput debug output or local configuration details. <br>
Risk: Transfer URLs or magnets submitted through the skill affect the user's put.io account. <br>
Mitigation: Submit only transfer URLs or magnets the user intentionally wants added to the account. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/baanish/skills/putio) <br>
- [put.io device-code login](https://put.io/link) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Rust, Cargo, the unofficial kaput CLI, and local device-code authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

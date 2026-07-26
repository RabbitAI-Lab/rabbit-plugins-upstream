## Description: <br>
Store, retrieve, list, and remove GPG-encrypted secrets using the pass password-store with a specified GPG key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators can use this skill to manage local password-store secrets from an agent workflow, including storing, retrieving, listing, removing, and exporting secrets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is environment-specific because it uses a hardcoded GPG recipient and the user's local pass store. <br>
Mitigation: Only use it when the configured GPG private key is under your control and the target pass store is intentional. <br>
Risk: Retrieval and environment export commands can expose secrets in an agent session, shell history, or logs. <br>
Mitigation: Review commands before execution and avoid printing or exporting secrets into shared sessions or persistent logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/pass-secrets) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce commands that read from or write to a local pass password store.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

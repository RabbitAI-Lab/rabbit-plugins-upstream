## Description: <br>
Operate Flexmail (flexmail.be) for reading, creating, updating, and deleting data instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate a connected Flexmail account through OOMOL for contact, subscription, interest, and account-configuration workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify Flexmail data, including creating or updating contacts and interests. <br>
Mitigation: Review write payloads and confirm the intended effect before execution. <br>
Risk: The skill exposes destructive actions such as unsubscribing contacts, deleting interests, and removing subscriptions. <br>
Mitigation: Require explicit approval for the exact destructive target before running the action. <br>
Risk: The skill depends on the OOMOL oo CLI and a connected Flexmail account. <br>
Mitigation: Install and authenticate the CLI only when needed, and review the CLI installer source if it is not already installed. <br>


## Reference(s): <br>
- [Flexmail homepage](https://flexmail.be/en) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON request or response data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing Flexmail action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

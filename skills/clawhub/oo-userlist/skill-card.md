## Description: <br>
Operate Userlist through an OOMOL-connected account, including reading records and creating or updating users, companies, relationships, events, and transactional messages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to run Userlist connector actions through the oo CLI for customer, company, relationship, event, and transactional messaging workflows. It is intended for agents working with a Userlist account that has already been connected through OOMOL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports that create-or-update actions are mislabeled as untagged actions, which could let an agent change Userlist customer or business data without confirmation. <br>
Mitigation: Treat push_user, push_company, and push_relationship as write actions and require explicit user confirmation of the exact payload before execution. <br>
Risk: Connector actions can create events, send transactional messages, and update users, companies, or relationships in a connected Userlist account. <br>
Mitigation: Fetch the live action schema before building payloads, review the target account and action effect, and run only with a Userlist account where these changes are acceptable. <br>


## Reference(s): <br>
- [ClawHub Userlist skill page](https://clawhub.ai/oomol/skills/oo-userlist) <br>
- [oo CLI repository](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Userlist homepage](https://userlist.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute oo CLI connector schema and run commands that return JSON responses from Userlist.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

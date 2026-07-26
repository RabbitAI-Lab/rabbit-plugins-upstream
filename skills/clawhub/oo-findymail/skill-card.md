## Description: <br>
Findymail (findymail.com) enables an agent to search, read, and verify professional email data through an OOMOL-connected Findymail account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and business users can use this skill to let an agent check Findymail credits, search for professional contacts by person or company domain, search employees, and verify professional email addresses through a connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Findymail searches and email verification may consume Findymail or OOMOL credits. <br>
Mitigation: Check remaining credits when relevant and run searches or verification only when the user intends to spend account credits. <br>
Risk: The skill can return professional contact data from Findymail. <br>
Mitigation: Handle returned contact data according to the user's business purpose and applicable privacy or data-handling requirements. <br>
Risk: First-time CLI installation, sign-in, and account connection steps affect the user's local environment or connected account. <br>
Mitigation: Run setup steps only when an action fails due to a missing CLI, authentication issue, or missing/expired Findymail connection. <br>


## Reference(s): <br>
- [Findymail homepage](https://www.findymail.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-findymail) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before execution; responses include connector data and an execution id when actions run.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

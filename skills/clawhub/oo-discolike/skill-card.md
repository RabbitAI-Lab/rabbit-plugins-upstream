## Description: <br>
DiscoLike helps agents discover companies and retrieve firmographic, digital footprint, SSL certificate, growth, usage, and billing data for a connected DiscoLike account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, developers, and agents use this skill to search DiscoLike for company matches and retrieve company profile, footprint, certificate, growth, and usage information from an already connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: DiscoLike queries are mediated through OOMOL for the user's connected account. <br>
Mitigation: Install and use the skill only after accepting OOMOL as an intermediary for DiscoLike access. <br>
Risk: The get_usage action can expose account usage and billing counters. <br>
Mitigation: Treat get_usage results as account and billing information and share them only with authorized users. <br>
Risk: Future connector actions that write, overwrite, or delete data could affect DiscoLike state. <br>
Mitigation: Require confirmation for write actions and explicit approval for destructive actions before execution. <br>


## Reference(s): <br>
- [DiscoLike homepage](https://discolike.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-discolike) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-oriented connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include account usage and billing counters when the get_usage action is requested.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

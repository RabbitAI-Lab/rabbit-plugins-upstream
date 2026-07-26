## Description: <br>
Operates Plunk through an OOMOL-connected account using the oo CLI for contact management, transactional email, event tracking, and email verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect Plunk connector schemas and run Plunk actions through the oo CLI. It supports contact management, transactional email sending, contact event tracking, and email verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write and destructive Plunk actions can change or delete real contact data, send transactional email, or record contact events. <br>
Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive commands. <br>
Risk: The skill depends on a trusted oo CLI session connected to the user's Plunk account. <br>
Mitigation: Use the oo CLI only for Plunk connector actions, and review payloads carefully before approving commands that affect Plunk data. <br>


## Reference(s): <br>
- [Plunk homepage](https://www.useplunk.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include oo CLI commands, connector schema lookups, and JSON payloads for Plunk actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

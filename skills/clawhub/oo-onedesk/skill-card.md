## Description: <br>
OneDesk helps agents search and read OneDesk work items, projects, and organization profile data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill when they need an agent to search OneDesk and retrieve item, project, or organization details without handling raw API tokens. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and search OneDesk data through the user's connected OOMOL account. <br>
Mitigation: Install it only for users who intend that access, scope requests narrowly, and review broad or sensitive searches before running them. <br>
Risk: First-time CLI installation, login, and OneDesk connection setup require local or account-level changes. <br>
Mitigation: Run setup only after an auth or connection failure, and approve install, login, and connection steps separately. <br>
Risk: Connector input schemas may change over time. <br>
Mitigation: Fetch the live action schema before constructing each JSON payload. <br>


## Reference(s): <br>
- [OneDesk homepage](https://www.onedesk.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing JSON payloads; read actions return OneDesk data with meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

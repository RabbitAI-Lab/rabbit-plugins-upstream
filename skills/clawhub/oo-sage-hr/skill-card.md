## Description: <br>
Use this skill to search and read Sage HR data through an OOMOL-connected account and the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and business users use this skill to let an agent retrieve Sage HR employee, team, position, termination, and time-off information from their connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose sensitive HR records, including employee, termination, and time-off data. <br>
Mitigation: Install it only when the agent should read Sage HR data through the user's OOMOL-connected account, and treat returned HR data as sensitive. <br>
Risk: Connector requests may be incorrect if the agent relies on stale action inputs. <br>
Mitigation: Inspect the live action schema before constructing a payload, and review any setup or connection step before proceeding. <br>


## Reference(s): <br>
- [Sage HR ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sage-hr) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Sage HR homepage](https://www.sage.com/en-us/sage-business-cloud/people/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses read-only Sage HR connector actions and live action schemas before payload construction.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

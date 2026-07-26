## Description: <br>
This skill helps agents use OOMOL's Check connector to inspect schemas and run supported Check actions for reading tax agency data and validating US addresses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators working with Check use this skill to retrieve or list tax agencies and validate US addresses through an OOMOL-connected Check account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on OOMOL's oo CLI and an OOMOL-connected Check account. <br>
Mitigation: Install only if OOMOL's CLI is trusted, review install commands before running them, and connect Check intentionally. <br>
Risk: Address validation may send address data through OOMOL to Check. <br>
Mitigation: Use address validation only when appropriate for the user's Check workflow and avoid sending unnecessary address data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-check) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Check homepage](https://www.checkhq.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; command responses include data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

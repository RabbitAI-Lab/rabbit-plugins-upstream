## Description: <br>
Luma (lu.ma) helps an agent search and read Luma account data through the OOMOL oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect Luma connector schemas and run read-only Luma actions for calendars, events, guests, and the current user profile through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Luma calendar, event, guest, and profile reads may expose sensitive account data. <br>
Mitigation: Review the Luma connection scopes in OOMOL and run read actions only for data the user requested. <br>
Risk: Future connector actions tagged write or destructive could change or remove Luma data. <br>
Mitigation: Require explicit confirmation of the exact payload, target, and effect before running those actions. <br>
Risk: Authentication, connection, credential, scope, or billing failures may require account setup steps. <br>
Mitigation: Run setup, connection, or billing steps only after a matching command failure and clear user intent. <br>


## Reference(s): <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Luma homepage](https://lu.ma) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include data and meta.executionId when returned by the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: skill metadata and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

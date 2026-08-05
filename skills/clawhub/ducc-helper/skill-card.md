## Description: <br>
ducc-helper lets an agent read, draft-edit, delete, and publish JD DUCC configuration through command-line scripts using local JingME/JD authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oilvegetable](https://clawhub.ai/user/oilvegetable) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations engineers use this skill to inspect DUCC namespaces, configuration files, profiles, and key-value items, then make draft changes and publish selected keys when authorized. It is intended for JD DUCC environments where the agent is allowed to use the operator's local JingME/JD login. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use local JingME/JD authentication to read, change, and publish DUCC configuration, including production configuration. <br>
Mitigation: Install it only where the agent is authorized to use that local login, and require explicit user confirmation before set, update, delete, or release actions. <br>
Risk: Configuration values and command output may contain sensitive operational data. <br>
Mitigation: Treat all read output as sensitive and avoid unnecessary sharing, logging, or persistence of returned values. <br>
Risk: Running lib/jme_auth.py directly prints the authentication cookie. <br>
Mitigation: Use the higher-level DUCC scripts instead of invoking the authentication helper directly. <br>
Risk: The security evidence calls out HTTP credential transport and broad dependency pinning for review before production use. <br>
Mitigation: Review credential transport and pin dependencies to approved versions before production deployment. <br>


## Reference(s): <br>
- [DUCC API Reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/oilvegetable/skills/ducc-helper) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read commands return JSON on stdout; write and release workflows can affect DUCC drafts or published configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Attio CRM integration for managing companies, people, deals, notes, tasks, and custom objects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[capt-marbles](https://clawhub.ai/user/capt-marbles) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, sales operators, and CRM teams use this skill to guide an agent in searching Attio records, managing companies and people, updating deals and pipelines, and creating notes or tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to create or update live Attio CRM records, pipeline entries, notes, and tasks. <br>
Mitigation: Require explicit approval before running commands that create, update, add, or complete CRM data. <br>
Risk: The skill uses an Attio API key that may be stored in the environment or `~/.env`. <br>
Mitigation: Use a least-privilege Attio token and avoid committing or sharing files that contain credentials. <br>
Risk: Commands assume the `attio` CLI being invoked is the intended tool. <br>
Mitigation: Verify the installed `attio` CLI before allowing an agent to run CRM operations. <br>


## Reference(s): <br>
- [Attio API Docs](https://docs.attio.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance commonly references the ATTIO_API_KEY environment variable and Attio CLI commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

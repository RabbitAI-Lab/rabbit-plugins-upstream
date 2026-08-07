## Description: <br>
Allows the user to record custom data annotations and agent visibility metrics, and generates simple HTML dashboards for visualization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fulcra](https://clawhub.ai/user/fulcra) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to define custom Fulcra tracking schemas, record selected annotations through the Fulcra CLI, and create lightweight visibility previews for tracked data and agent activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to send sensitive personal tracking data, such as health, location, messaging, or memory-derived details, to a Fulcra account. <br>
Mitigation: Use explicit user opt-in, keep tracked fields minimal, and confirm the exact data before recording it. <br>
Risk: Incorrect deletion or correction commands could remove or replace the wrong Fulcra record. <br>
Mitigation: Show the exact data type and record ID before deleting or correcting stored data. <br>


## Reference(s): <br>
- [Fulcra CLI for Tracking & Dashboards](references/fulcra-tracking-cli.md) <br>
- [Fulcra High-Impact Use Cases](references/fulcra-tracking-usecases.md) <br>
- [Fulcra CLI Documentation](https://raw.githubusercontent.com/fulcradynamics/agent-skills/main/skills/fulcra-onboarding/references/fulcra-cli.md) <br>
- [Fulcra Agent Skills](https://github.com/fulcradynamics/agent-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with inline bash commands and optional single-file HTML preview code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may produce Fulcra CLI commands and lightweight HTML previews based on user-selected tracking fields.] <br>

## Skill Version(s): <br>
0.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

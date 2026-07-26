## Description: <br>
Allows the user to record custom data annotations and agent visibility metrics, and generates simple HTML dashboards for visualization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fulcra](https://clawhub.ai/user/fulcra) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to discover useful Fulcra tracking workflows, create custom annotation schemas, record initial data with consent, and generate a static HTML dashboard that visualizes the recorded data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may involve sensitive personal data such as health, location, calendar, media history, prior chat context, or agent-activity logs. <br>
Mitigation: Review each prompt before authorizing collection, decline data sources you do not want persisted, and enable only the Fulcra features you are comfortable using. <br>
Risk: Recorded annotations are sent to the user's Fulcra account and may persist in a personal datastore. <br>
Mitigation: Require explicit user consent before transmitting user-provided tracking data and explain what will be stored. <br>
Risk: Fulcra API access tokens are sensitive credentials. <br>
Mitigation: Inject tokens at command execution time and avoid storing them in files or printing them in chat. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/fulcra/skills/fulcra-tracking) <br>
- [Fulcra Agent Skills Repository](https://github.com/fulcradynamics/agent-skills) <br>
- [Fulcra CLI for Tracking & Dashboards](references/fulcra-tracking-cli.md) <br>
- [Fulcra Onboarding: Discovery](references/fulcra-tracking-discovery.md) <br>
- [Fulcra Record Annotations](references/fulcra-tracking-record-annotations.md) <br>
- [Fulcra Onboarding: Demonstration](references/fulcra-tracking-demonstration.md) <br>
- [Fulcra High-Impact Use Cases](references/fulcra-tracking-usecases.md) <br>
- [Fulcra CLI Documentation](https://raw.githubusercontent.com/fulcradynamics/agent-skills/main/skills/fulcra-onboarding/references/fulcra-cli.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated static HTML dashboard files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local HTML, CSS, and JavaScript dashboard artifacts after user confirmation.] <br>

## Skill Version(s): <br>
0.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

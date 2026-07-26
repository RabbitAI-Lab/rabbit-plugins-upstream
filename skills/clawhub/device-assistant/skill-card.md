## Description: <br>
Personal device and appliance manager with error code lookup, troubleshooting, warranty tracking, manual links, and maintenance reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[udiedrichsen](https://clawhub.ai/user/udiedrichsen) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users use this skill to maintain a personal inventory of household devices, appliances, electronics, and software, then look up manuals, warranty status, maintenance needs, and device-specific troubleshooting guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Device inventory records may include model numbers, serial numbers, purchase details, warranty records, locations, and notes stored in workspace memory. <br>
Mitigation: Store only necessary device details, avoid unnecessary serial numbers or purchase records, and review workspace access before sharing. <br>
Risk: Generated manual, support, or search links may include model numbers, error codes, or household device details that can be sent to third-party sites if opened. <br>
Mitigation: Review generated links and search queries before opening them, and remove sensitive terms when possible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/udiedrichsen/skills/device-assistant) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [JSON responses with text guidance, device records, status summaries, and generated manual or support links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores device inventory, error history, maintenance logs, and cached lookup metadata under workspace memory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

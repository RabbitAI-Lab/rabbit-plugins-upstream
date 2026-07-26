## Description: <br>
Prospect and enrich contacts via the SignalHire API (Search, Person and Credits). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ms-youssef](https://clawhub.ai/user/ms-youssef) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an OpenClaw agent check SignalHire credits, search for prospects, and enrich contact records through an asynchronous callback workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a publicly reachable callback endpoint for asynchronous enrichment results. <br>
Mitigation: Expose the callback only through a hardened proxy or tunnel, require verification where possible, and monitor that it returns HTTP 200 promptly. <br>
Risk: The connector stores enriched personal contact details in local CSV files. <br>
Mitigation: Restrict the output directory, keep CSV files out of shared storage and source control, and define retention and deletion rules before use. <br>
Risk: Using enriched contact data may create privacy or compliance obligations. <br>
Mitigation: Review applicable privacy requirements, data-subject rights, and opt-out handling before collecting or using contact records. <br>


## Reference(s): <br>
- [SignalHire API documentation](https://www.signalhire.com/api/person) <br>
- [ClawHub skill listing](https://clawhub.ai/ms-youssef/skills/signalhire-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code snippets, shell commands, API request guidance, JSON status responses, and CSV files from the connector.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SIGNALHIRE_API_KEY and SIGNALHIRE_CALLBACK_URL; the connector writes per-job and consolidated CSV files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

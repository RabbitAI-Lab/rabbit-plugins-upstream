## Description: <br>
Analyzes top-down lawn images, videos, or URLs to estimate yellowing, weed coverage, bare soil, and an overall lawn health score with maintenance-oriented guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Support lawn managers, homeowners, golf course operators, park teams, and sports-field maintainers by turning supported lawn media into structured health assessment results, report links, and care direction. <br>

### Deployment Geography for Use: <br>
No deployment geography restriction is stated in the evidence; use only where ClawHub, the publisher service, and local data-handling requirements permit this workflow. <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says the skill uses a cloud workflow for lawn images or videos, submitted URLs, account identifiers, report history, and locally stored service tokens. <br>
Mitigation: Install only when that data can be handled by the publisher's external services, and review identity and data-retention behavior before use. <br>
Risk: The security evidence says the skill silently creates or reuses an identity and exposes historical reports. <br>
Mitigation: Use a dedicated workspace for sensitive projects, avoid shared machines for report retrieval, and clear local identity or token state when access should not persist. <br>
Risk: The server security verdict is suspicious. <br>
Mitigation: Review the ClawHub security summary before installation and run the skill in a constrained environment until the external-service and token-storage behavior is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-lawn-health-assessment-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Structured lawn assessment report with yellowing ratio, weed coverage, bare-soil signals, health score, care guidance, report links, and optional historical report listings.] <br>
**Output Parameters:** [Accepts a local media path or network URL, optional detail level, optional output path, and a list mode for cloud report history.] <br>
**Other Properties Related to Output:** [Uses a publisher cloud workflow for analysis and history retrieval; outputs may include report export links and service-returned structured data.] <br>

## Skill Version(s): <br>
1.0.4 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

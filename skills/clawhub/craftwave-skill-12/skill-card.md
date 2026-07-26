## Description: <br>
A cruise search tool that helps users find cruise products by keyword. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this tool to search for cruise products by keyword through a remote MCP tool. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cruise-search queries are sent to a remote CruiseSkillBridge/olavacations service. <br>
Mitigation: Avoid entering sensitive personal, booking, account, or payment details unless the publisher documents how that data is handled. <br>
Risk: Documentation for the remote service and data handling is incomplete. <br>
Mitigation: Review publisher documentation and test with non-sensitive queries before using the skill in workflows that handle customer or booking information. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/309441738/skills/craftwave-skill-12) <br>
- [CruiseSkillBridge](https://cruiseskillbridge.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, API calls] <br>
**Output Format:** [Remote MCP tool response, typically text or JSON-like structured cruise search results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results depend on the remote CruiseSkillBridge/olavacations service and the user's search terms.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

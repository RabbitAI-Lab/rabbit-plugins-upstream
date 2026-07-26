## Description: <br>
Trello API integration with managed OAuth for managing boards, lists, cards, checklists, labels, and members through Maton. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to read and manage Trello project data through a Maton-managed OAuth connection. It supports board, list, card, checklist, label, member, search, and connection workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and modify Trello boards, lists, cards, labels, checklists, and membership assignments through the connected account. <br>
Mitigation: Install only when Maton is trusted to broker Trello OAuth access, and confirm every create, update, or delete action before it runs. <br>
Risk: Requests may target the wrong Trello account when multiple OAuth connections are active. <br>
Mitigation: Use the intended Trello connection explicitly when multiple connections exist. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/trello-api) <br>
- [Publisher Profile](https://clawhub.ai/user/byungkyu) <br>
- [Maton API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway) <br>
- [Trello API Overview](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/) <br>
- [Trello Boards API](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/) <br>
- [Trello Lists API](https://developer.atlassian.com/cloud/trello/rest/api-group-lists/) <br>
- [Trello Cards API](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/) <br>
- [Trello Checklists API](https://developer.atlassian.com/cloud/trello/rest/api-group-checklists/) <br>
- [Trello Labels API](https://developer.atlassian.com/cloud/trello/rest/api-group-labels/) <br>
- [Trello Members API](https://developer.atlassian.com/cloud/trello/rest/api-group-members/) <br>
- [Trello Search API](https://developer.atlassian.com/cloud/trello/rest/api-group-search/) <br>
- [Maton CLI Manual](https://cli.maton.ai/manual) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash, Python, JavaScript, HTTP, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and an active Trello OAuth connection. Write operations should be confirmed before execution.] <br>

## Skill Version(s): <br>
1.0.6 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

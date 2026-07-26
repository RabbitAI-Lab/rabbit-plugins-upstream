## Description: <br>
Search and retrieve ServiceNow documentation, release notes, and developer docs (APIs, references, guides). Uses docs.servicenow.com via Zoomin and developer.servicenow.com APIs for developer topics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesethrose](https://clawhub.ai/user/thesethrose) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, administrators, and support teams use this skill to find ServiceNow platform documentation, release notes, scripting references, and developer guides for answering ServiceNow implementation and troubleshooting questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The article-fetching tool can be directed to fetch arbitrary URLs. <br>
Mitigation: Review before installing in environments with private networks or sensitive internal services; prefer a version that restricts article fetching to HTTPS ServiceNow documentation domains or URLs returned by the search tool. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thesethrose/skills/servicenow-docs) <br>
- [ServiceNow Documentation](https://docs.servicenow.com/) <br>
- [ServiceNow Zoomin Search API](https://servicenow-be-prod.servicenow.com/search) <br>
- [ServiceNow Developer Search API](https://developer.servicenow.com/api/now/uxf/databroker/exec) <br>
- [ServiceNow Developer Suggest API](https://developer.servicenow.com/api/now/graphql) <br>
- [ServiceNow Developer Guides API](https://developer.servicenow.com/api/snc/v1/guides) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown summaries with ranked search results, documentation URLs, short excerpts, and concise error messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Some developer API reference results return URLs only; article and guide content may be truncated.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

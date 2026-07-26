## Description: <br>
LinkedIn Community Management API integration with managed OAuth for organization pages, posts, comments, reactions, and analytics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage LinkedIn organization content through Maton-managed OAuth, including creating posts, editing or deleting posts and comments, reacting to content, looking up organizations, and retrieving page or follower statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, edit, delete, comment on, or react to LinkedIn content, which can affect a public or business LinkedIn presence. <br>
Mitigation: Confirm the exact Maton connection, LinkedIn identity, target organization, target resource, and content before allowing write actions. <br>
Risk: Requests act within the permissions granted to the connected LinkedIn account. <br>
Mitigation: Verify the intended Maton connection and LinkedIn organization before performing actions, especially when multiple connections are available. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/linkedin-community) <br>
- [Maton](https://maton.ai) <br>
- [LinkedIn Community Management Overview](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-overview) <br>
- [LinkedIn Posts API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api) <br>
- [LinkedIn Comments API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/comments-api) <br>
- [LinkedIn Reactions API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/reactions-api) <br>
- [LinkedIn Organization Lookup API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/organization-lookup-api) <br>
- [LinkedIn Follower Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/follower-statistics) <br>
- [LinkedIn Page Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/page-statistics) <br>
- [LinkedIn Share Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/share-statistics) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl commands, JSON payloads, and JavaScript or Python examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, a valid MATON_API_KEY, and a Maton LinkedIn OAuth connection.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

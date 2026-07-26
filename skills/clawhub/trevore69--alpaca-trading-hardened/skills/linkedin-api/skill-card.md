## Description: <br>
LinkedIn API integration with managed OAuth for sharing posts, managing profiles and organizations, uploading media, accessing ad library data, and using advertising features when the connected account has the required scopes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to make LinkedIn API requests through Maton-managed OAuth, including profile lookup, organization access, media uploads, social posting, public ad library searches, and advertising workflows. It is appropriate when the user has a valid Maton API key and has reviewed the LinkedIn OAuth scopes granted to the connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish LinkedIn posts or modify resources when the connected account has write scopes. <br>
Mitigation: Require explicit user confirmation before public posts and before any create, update, or delete request; show the operation and request body or key parameters first. <br>
Risk: Advertising workflows can change ad accounts, campaigns, budgets, targeting, or other settings with financial impact. <br>
Mitigation: Verify granted advertising scopes and confirm budget amounts, targeting criteria, ad account IDs, and campaign state before sending advertising requests. <br>
Risk: Multiple LinkedIn OAuth connections can cause requests to affect the wrong account. <br>
Mitigation: Use the Maton-Connection header whenever more than one LinkedIn connection exists. <br>
Risk: Delete operations may be irreversible or remove associated campaign data. <br>
Mitigation: Confirm the exact resource ID, current status, and unrecoverable nature of the deletion before executing destructive requests. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/linkedin-api) <br>
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway) <br>
- [LinkedIn API Overview](https://learn.microsoft.com/en-us/linkedin/) <br>
- [Share on LinkedIn Guide](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin) <br>
- [Profile API](https://learn.microsoft.com/en-us/linkedin/shared/integrations/people/profile-api) <br>
- [Sign In with LinkedIn](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin-v2) <br>
- [LinkedIn Authentication Guide](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication) <br>
- [LinkedIn Marketing API](https://learn.microsoft.com/en-us/linkedin/marketing/) <br>
- [LinkedIn Ad Accounts](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-accounts) <br>
- [LinkedIn Campaign Management](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-campaigns) <br>
- [LinkedIn Ad Library API](https://www.linkedin.com/ad-library/api/) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with inline HTTP examples and Python or JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, LinkedIn-Version headers, and account-specific OAuth scopes.] <br>

## Skill Version(s): <br>
1.0.9 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

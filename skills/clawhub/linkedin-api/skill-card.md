## Description: <br>
LinkedIn API integration with managed OAuth for sharing posts, managing profile and organization data, uploading media, accessing the Ad Library, and managing advertising features. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect agents to LinkedIn through Maton-managed OAuth, retrieve LinkedIn profile or organization information, publish content, upload media, and work with advertising workflows after user approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill gives Maton-mediated access to the connected LinkedIn account. <br>
Mitigation: Install only when comfortable with that access model, keep MATON_API_KEY protected, and verify the connected account and granted OAuth scopes before use. <br>
Risk: Public posts, organization actions, and profile changes can affect reputation. <br>
Mitigation: Show the exact operation and request body or key parameters, then wait for explicit user confirmation before any create, update, or delete request. <br>
Risk: Advertising operations can change budgets, targeting, campaigns, or ad accounts and may spend money. <br>
Mitigation: Confirm budget amounts, targeting criteria, ad account identifiers, and campaign status with the user before sending advertising requests. <br>
Risk: Destructive LinkedIn operations may be irreversible. <br>
Mitigation: Confirm the resource identifier and explain that deletion may not be recoverable before sending DELETE requests. <br>


## Reference(s): <br>
- [ClawHub LinkedIn skill listing](https://clawhub.ai/byungkyu/skills/linkedin-api) <br>
- [LinkedIn API Overview](https://learn.microsoft.com/en-us/linkedin/) <br>
- [Share on LinkedIn Guide](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin) <br>
- [LinkedIn Marketing API](https://learn.microsoft.com/en-us/linkedin/marketing/) <br>
- [LinkedIn Advertising Policies](https://www.linkedin.com/legal/ads-policy) <br>
- [Maton settings](https://maton.ai/settings) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with inline code blocks and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MATON_API_KEY, network access, LinkedIn-Version: 202606, and appropriate LinkedIn OAuth scopes.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata, released 2026-07-24) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

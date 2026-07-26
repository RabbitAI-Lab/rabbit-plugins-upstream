## Description: <br>
Create, schedule, and publish social media posts across Instagram, TikTok, YouTube, X, LinkedIn, Facebook, Pinterest, Threads, and Bluesky via the Social0 CLI or MCP, including account listing, media upload, drafts, instant publishing, scheduling, and per-platform publish status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abhishek-b-r](https://clawhub.ai/user/abhishek-b-r) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and social media operators use this skill to draft, schedule, and publish posts through Social0 from an agent conversation or terminal workflow. It is useful when an agent needs structured guidance for authentication, account selection, media upload, publishing, scheduling, and status polling across supported social platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help an agent publish real posts to connected social accounts. <br>
Mitigation: Use drafts for testing, review target accounts and platforms before publishing, and require clear user intent before live publish actions. <br>
Risk: Social0 API keys or connector credentials could allow access to connected publishing workflows if exposed. <br>
Mitigation: Keep the Social0 API key private, prefer secure login or hosted OAuth where available, avoid searching local secret stores, and revoke connector keys from the Social0 dashboard when no longer needed. <br>
Risk: Posts can target the wrong account or platform when multiple accounts are connected or when platform aliases are ambiguous. <br>
Mitigation: List accounts before the first publish in a session, use explicit account identifiers when needed, and poll publish status to confirm per-platform results. <br>


## Reference(s): <br>
- [Social0](https://social0.app) <br>
- [Social0 CLI documentation](https://docs.social0.app/docs/integrations/cli) <br>
- [Social0 MCP documentation](https://docs.social0.app/docs/integrations/mcp) <br>
- [Social0 API](https://api.social0.app/v1) <br>
- [Hosted Social0 MCP endpoint](https://mcp.social0.app/mcp) <br>
- [npm social0 package](https://www.npmjs.com/package/social0) <br>
- [npm @social0/mcp package](https://www.npmjs.com/package/@social0/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON configuration snippets, and API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Social0 CLI commands, MCP configuration snippets, REST fallback examples, publishing checklists, and status-polling guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

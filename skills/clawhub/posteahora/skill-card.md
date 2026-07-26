## Description: <br>
PosteAhora helps agents and developers schedule, draft, publish, manage, upload media for, and analyze social media posts across Instagram, TikTok, YouTube, X, Facebook, LinkedIn, Threads, Bluesky, and Discord. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sashadiz](https://clawhub.ai/user/sashadiz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and AI agents use this skill to automate social publishing workflows from the terminal, CI, or agent tooling. It supports authenticated account discovery, media upload, draft creation, scheduled publishing, immediate publishing, post status checks, idea backlog management, and analytics review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate PosteAhora-connected social accounts and publish outward-facing content. <br>
Mitigation: Prefer drafts or scheduled posts for review, and confirm the caption, target accounts, and timing before any live post. <br>
Risk: Uploaded media URLs may be public. <br>
Mitigation: Upload only media intended for public distribution and verify target platform requirements before attaching media to posts. <br>
Risk: The PosteAhora API key grants account access and may appear in shell history, logs, screenshots, or shared config files if mishandled. <br>
Mitigation: Keep the API key out of logs and screenshots, avoid echoing it, and prefer the POSTEAHORA_API_KEY environment variable or the CLI's auth storage. <br>
Risk: Wrong account IDs or stale scheduling details can send content to an unintended platform or time. <br>
Mitigation: Run posteahora accounts before publishing, use explicit platform:accountId targets, never guess IDs, and ensure scheduled times are future ISO 8601 timestamps. <br>


## Reference(s): <br>
- [Server-resolved GitHub import](https://github.com/SashaDiz/skills/tree/main/skills/posteahora) <br>
- [ClawHub listing](https://clawhub.ai/sashadiz/skills/posteahora) <br>
- [PosteAhora website](https://posteahora.com) <br>
- [PosteAhora documentation](https://posteahora.com/docs) <br>
- [PosteAhora API reference](https://posteahora.com/docs/api) <br>
- [PosteAhora CLI on npm](https://www.npmjs.com/package/@posteahora/cli) <br>
- [PosteAhora CLI on GitHub](https://github.com/posteahora/cli) <br>
- [PosteAhora MCP server](https://github.com/posteahora/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands can create drafts, schedule posts, publish live content, upload media to public URLs, list accounts and posts, and return machine-readable output with --json.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

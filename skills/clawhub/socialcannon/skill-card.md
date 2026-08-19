## Description:

Publish, schedule, and manage social media posts across Twitter/X, Facebook, Instagram, LinkedIn, TikTok, and YouTube, with content calendar gap analysis, A/B testing, engagement inbox, AI content repurposing, optimal timing suggestions, auto-scheduling, UTM tracking, and platform-native AI-content disclosure labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miprinia](https://clawhub.ai/user/miprinia)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill to connect SocialCannon credentials, inspect accounts and calendars, draft or schedule posts, manage engagement workflows, and call the SocialCannon REST API or optional MCP server for supported social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent act on real social accounts, including publishing, replying, retrying posts, deleting posts, disconnecting accounts, and repurposing content in post mode.

Mitigation: Keep credentials in environment variables, connect only intended accounts, prefer drafts or scheduled posts, and require explicit human approval before live or irreversible actions.

Risk: Platform-specific restrictions can cause failed posts or incomplete analytics and engagement workflows.

Mitigation: Check platform capabilities before acting, list accounts before creating posts, respect TikTok privacy requirements, and use preview or validation responses before publishing repurposed content.

## Reference(s):

- [SocialCannon homepage](https://socialcannon.app)
- [ClawHub skill page](https://clawhub.ai/miprinia/skills/socialcannon)
- [@socialcannon/mcp package](https://www.npmjs.com/package/@socialcannon/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl examples, JSON request and response examples, and MCP configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SocialCannon client credentials and curl for direct API examples; optional MCP usage uses the @socialcannon/mcp package.]

## Skill Version(s):

1.11.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

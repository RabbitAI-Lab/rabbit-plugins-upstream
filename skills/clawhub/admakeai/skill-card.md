## Description:

Create, edit, and ship ad creative through the AdMakeAI API, including ad images, edits, batch ad sets, ad copy, UGC video, Meta uploads, and analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mesmerlord](https://clawhub.ai/user/mesmerlord)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketers, and advertising operators use this skill to create ad creatives, generate copy, research competitors, prepare Meta campaign drafts, and report on Meta ads through an AdMakeAI account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend AdMakeAI credits through image, batch, video, and Meta upload workflows.

Mitigation: Require explicit user confirmation before any generation, upload, batch run, or other credit-spending action.

Risk: The skill can create Meta advertising objects or drafts when connected Meta accounts are used.

Mitigation: Review the target account, campaign, ad set, creative, and intended action with the user before any Meta write action.

Risk: Using the wrong project or brand can generate creatives against the wrong account context and spend credits.

Mitigation: List projects first, choose only when the user's intent clearly identifies a project, and ask for clarification when multiple projects remain plausible.

Risk: The AdMakeAI API key grants account access for ad workflows.

Mitigation: Keep ADMAKEAI_API_KEY in the environment and do not echo it, store it in files, or include it in user-visible output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mesmerlord/skills/admakeai)
- [Publisher profile](https://clawhub.ai/user/mesmerlord)
- [AdMakeAI homepage](https://admakeai.com)
- [AdMakeAI API documentation](https://admakeai.com/api/docs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with REST and MCP tool names, JSON payload examples, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, curl, an AdMakeAI account, and ADMAKEAI_API_KEY.]

## Skill Version(s):

1.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

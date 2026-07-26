## Description: <br>
Access a user's personal Miremo knowledge base and reusable method skills to search notes, browse documents and tags, explore knowledge graph context, save new memos, and retrieve method materials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hansenz42](https://clawhub.ai/user/hansenz42) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill in OpenClaw to connect an authenticated Miremo account, research their own notes, documents, tags, and knowledge graph, save new memos, and retrieve reusable method skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Miremo API key, which could expose the user's Miremo account if committed, synced, or shared accidentally. <br>
Mitigation: Store the key only in local OpenClaw MCP configuration, keep it out of version control and synced dotfiles, and revoke it in Miremo settings if exposure is suspected. <br>
Risk: The skill can read the authenticated user's Miremo content and create new memos when asked. <br>
Mitigation: Install and use it only when authenticated Miremo access is intended, and review requests that would save new information before allowing memo creation. <br>


## Reference(s): <br>
- [Miremo Research Skill on ClawHub](https://clawhub.ai/hansenz42/skills/miremo) <br>
- [Miremo website](https://www.miremoapp.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with tool call guidance and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference authenticated Miremo search results, memo IDs, document sections, workspace metadata, entity graph summaries, and created memo IDs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

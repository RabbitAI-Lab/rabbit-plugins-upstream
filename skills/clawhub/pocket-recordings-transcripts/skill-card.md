## Description: <br>
Pocket: Search, list, and read the user's Pocket recordings including transcripts and AI summaries; create audio download links; save recording audio to file storage; upload new audio recordings; list tags. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent search, list, read, summarize, upload, tag, and retrieve audio links for Pocket recordings through AgentPMT-hosted tool calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pocket transcripts, summaries, tags, and audio may contain confidential conversation data. <br>
Mitigation: Install only for users who intend agent access to Pocket recordings, keep requests scoped to the task, and treat returned recording content as confidential. <br>
Risk: Audio download, save, and upload actions can create or transmit copies of recordings through AgentPMT, Pocket, and File Manager. <br>
Mitigation: Prefer temporary one-time download URLs when practical and use save or upload actions only when creating or transmitting a copy is acceptable. <br>


## Reference(s): <br>
- [Generated action schema](artifact/schema.md) <br>
- [AgentPMT marketplace page](https://www.agentpmt.com/marketplace/pocket-recordings-transcripts) <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/pocket-recordings-transcripts) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, JSON, API calls, Configuration] <br>
**Output Format:** [Markdown instructions with JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defines seven AgentPMT actions for Pocket recordings, including search, listing, retrieval, temporary audio URLs, file saves, uploads, and tag listing.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

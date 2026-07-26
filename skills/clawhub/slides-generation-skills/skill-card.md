## Description: <br>
Generates presentations with the 2slides API from text content, reference image styles, or document summaries, with theme selection, multiple languages, and synchronous or asynchronous workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[javainthinking](https://clawhub.ai/user/javainthinking) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to create presentation decks from prompts, outlines, documents, or reference images through the 2slides API. It is suited for agents that need to search themes, generate slides, return slide or PDF links, and poll asynchronous generation jobs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Presentation prompts, document-derived summaries, and reference images are sent to the 2slides service for processing. <br>
Mitigation: Avoid confidential, regulated, or proprietary material unless approved for external processing. <br>
Risk: 2slides API keys can be exposed through URLs, logs, screenshots, shell history, or shared configuration. <br>
Mitigation: Prefer the environment-variable Python workflow, do not commit or share configuration containing keys, and rotate any key that may have been exposed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/javainthinking/skills/slides-generation-skills) <br>
- [2slides Website](https://2slides.com) <br>
- [2slides API Portal](https://2slides.com/api) <br>
- [2slides API Reference](references/api-reference.md) <br>
- [MCP Integration Guide](references/mcp-integration.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON API responses, and presentation or PDF URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return slideUrl and pdfUrl links for completed jobs, or jobId values for asynchronous polling.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

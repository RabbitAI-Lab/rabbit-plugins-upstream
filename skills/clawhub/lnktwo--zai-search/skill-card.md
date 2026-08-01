## Description: <br>
Free live web search powered by Z.AI GLM-4.5-Flash with built-in web_search tool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lnktwo](https://clawhub.ai/user/lnktwo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to run live web searches, optionally limit result count, filter by domain, and receive Markdown-formatted sources and summaries through a Z.AI API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and the bearer token are sent to Z.AI, or to the URL in ZAI_BASE_URL if that environment variable is set. <br>
Mitigation: Use a trusted Z.AI-compatible endpoint only, keep ZAI_BASE_URL unset unless intentionally configured, and avoid sending sensitive queries unless permitted by the user's data-handling policy. <br>


## Reference(s): <br>
- [Z.AI Web Search Documentation](https://docs.z.ai/guides/tools/web-search) <br>
- [ClawHub Skill Page](https://clawhub.ai/lnktwo/skills/zai-search) <br>
- [Publisher Profile](https://clawhub.ai/user/lnktwo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown search results with source URLs and concise summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports result limits up to 20, optional domain filtering, and raw mode.] <br>

## Skill Version(s): <br>
1.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Search the web using Google Custom Search Engine (PSE). Use this when you need live information, documentation, or to research topics and the built-in web_search is unavailable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mxfeinberg](https://clawhub.ai/user/mxfeinberg) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external agent users use this skill to let OpenClaw agents run live web searches through Google Programmable Search Engine when built-in web search is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Google's Custom Search API. <br>
Mitigation: Avoid confidential search text and use the skill only where sending queries to Google is acceptable. <br>
Risk: The skill requires a Google API key and Programmable Search Engine ID. <br>
Mitigation: Use a restricted API key, provide credentials through environment variables or a private .env file, and keep credential files out of source control. <br>


## Reference(s): <br>
- [Google Programmable Search Engine](https://cse.google.com/cse/all) <br>
- [Google Custom Search API endpoint](https://www.googleapis.com/customsearch/v1) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration] <br>
**Output Format:** [JSON search results plus Markdown setup and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GOOGLE_API_KEY and GOOGLE_CSE_ID environment variables; returns five results by default unless a result count is provided.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

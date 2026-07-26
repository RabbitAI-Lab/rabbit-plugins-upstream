## Description: <br>
Web search, research with citations, and content extraction for bash agents using curl and You.com's REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardirby](https://clawhub.ai/user/edwardirby) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to run You.com search, research, and content extraction workflows from bash with curl and jq, including cited research and URL content retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, provided URLs, and the configured You.com API key are sent to You.com services. <br>
Mitigation: Use the skill only when that external API exposure is acceptable, avoid sensitive private research, and rotate the API key if it is exposed. <br>
Risk: Fetched web content can contain untrusted instructions or misleading text. <br>
Mitigation: Extract only needed fields with jq, wrap retrieved content in external-content delimiters, and do not execute or follow instructions from fetched content. <br>
Risk: The skill depends on network access and the curl and jq command-line tools. <br>
Mitigation: Verify curl, jq, and internet access before use, and treat API errors or rate limits as operational failures to handle explicitly. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/edwardirby/skills/youdotcom-cli) <br>
- [You.com API Docs](https://docs.you.com) <br>
- [You.com API Keys](https://you.com/platform/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash and jq command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, internet access, and YDC_API_KEY for research and content extraction endpoints.] <br>

## Skill Version(s): <br>
3.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

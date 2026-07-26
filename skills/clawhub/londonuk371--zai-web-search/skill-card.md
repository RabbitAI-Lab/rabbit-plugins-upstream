## Description: <br>
Searches the web through the Z.AI Web Search API and returns plain-text search results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[londonuk371](https://clawhub.ai/user/londonuk371) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when a task requires current web information, source lookup, or search results beyond the model's training data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to the external Z.AI Web Search API. <br>
Mitigation: Do not include passwords, tokens, private workspace content, personal data, or confidential business information in queries. <br>
Risk: The skill requires a ZAI API key from the environment or a local key file. <br>
Mitigation: Store the API key outside shared files and review shell commands before running the search script. <br>


## Reference(s): <br>
- [Z.AI Web Search documentation](https://docs.z.ai/guides/tools/web-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text search results with titles, URLs, and summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search count is optional, defaults to 5, and is documented with a maximum of 50.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

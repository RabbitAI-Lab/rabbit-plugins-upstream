## Description: <br>
Use the Kagi API Search API and FastGPT for web research, ranked search results, and summarized answers with citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[michaelasper](https://clawhub.ai/user/michaelasper) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to call Kagi Search API for ranked web results or FastGPT for grounded summaries with citation references, especially when another search provider is rate-limited or lower quality. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and FastGPT prompts are sent to Kagi using the user's API token. <br>
Mitigation: Avoid submitting secrets, personal data, or regulated information in queries or prompts. <br>
Risk: API calls may consume Kagi quota. <br>
Mitigation: Use the skill only when Kagi search or FastGPT is needed and monitor API usage against the account quota. <br>


## Reference(s): <br>
- [Kagi API quick reference](references/kagi-api.md) <br>
- [Kagi API documentation](https://help.kagi.com/kagi/api/) <br>
- [Kagi API token settings](https://kagi.com/settings/api) <br>
- [ClawHub skill page](https://clawhub.ai/michaelasper/skills/kagi) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Plain text or JSON from command-line API wrappers; FastGPT output may include citation references.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided Kagi API token and may consume Kagi API quota.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

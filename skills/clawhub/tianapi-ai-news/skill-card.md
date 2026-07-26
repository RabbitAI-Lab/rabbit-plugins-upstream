## Description: <br>
Aggregates news about artificial intelligence, large models, and algorithms with keyword search and pagination through TianAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve current AI news, search for topic-specific updates such as large-model news, and present titles, sources, publication times, and links to users. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the TianAPI API key and search terms to TianAPI when fetching news. <br>
Mitigation: Use the skill only when TianAPI is an acceptable recipient, inject the key through an environment variable or secret manager, and avoid passing credentials on the command line. <br>
Risk: Credential setup may fail because the documented environment variable differs from the script's variable name. <br>
Mitigation: Verify the required environment variable before use and prefer a secret-managed environment value over a checked-in scripts/.env file. <br>
Risk: Command examples and the script interface are inconsistent, including the documented JSON mode. <br>
Mitigation: Test the fetch command in a non-sensitive environment before relying on it in an agent workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/workxin/skills/tianapi-ai-news) <br>
- [TianAPI AI news API](https://www.tianapi.com/apiview/22) <br>
- [TianAPI](https://www.tianapi.com) <br>
- [TianAPI AI endpoint](https://apis.tianapi.com/ai/index) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; script output is human-readable text or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a TianAPI API key; supports result count, page, and keyword parameters.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

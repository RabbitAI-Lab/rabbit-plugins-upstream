## Description: <br>
Post to X (Twitter) using the official API with OAuth 1.0a. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lobstergeneralintelligence](https://clawhub.ai/user/lobstergeneralintelligence) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to publish tweets or updates through the official X API when cookie-based posting is unreliable or blocked. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish public posts from the configured X account. <br>
Mitigation: Review tweet text before running the command and use the skill only when posting from that account is intended. <br>
Risk: X API credentials may be exposed through environment variables or local configuration files. <br>
Mitigation: Protect the token file, avoid committing credentials, remove unexpected .x-api.json files from project directories, and do not post secrets or private information. <br>
Risk: The npm dependency may change across installs when version ranges are used. <br>
Mitigation: Pin and review the twitter-api-v2 dependency when reproducible or controlled installs are required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lobstergeneralintelligence/skills/x-api) <br>
- [X Developer Platform](https://developer.x.com) <br>
- [X Developer Portal dashboard](https://developer.x.com/en/portal/dashboard) <br>
- [bird CLI](https://github.com/steipete/bird) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, Text] <br>
**Output Format:** [Markdown guidance with shell command examples; runtime command prints status text and a tweet URL.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Posts user-provided text to X using configured OAuth 1.0a credentials.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

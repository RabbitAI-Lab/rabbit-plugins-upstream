## Description: <br>
OmniSearch gives agents a mandatory wrapper for searching current web information, news, prices, facts, and other data that may not be available from static model knowledge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bguidolim](https://clawhub.ai/user/bguidolim) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use OmniSearch to route time-sensitive questions through configured web search providers and return summarized answers with source links. It is intended for current facts, news, prices, product research, and other information that may have changed since model training. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries may disclose sensitive information to the configured search provider. <br>
Mitigation: Avoid including secrets, private customer data, or sensitive local context in searches unless disclosure to that provider is intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bguidolim/skills/omnisearch) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown responses with summarized findings, source links, and inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search queries may be sent to configured third-party search providers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

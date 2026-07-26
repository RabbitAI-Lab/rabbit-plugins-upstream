## Description: <br>
Provides real-time US stock quotes and financial data using the Finnhub API and Python. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[keyfrog-21k](https://clawhub.ai/user/keyfrog-21k) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to fetch real-time US stock quote and financial data through Finnhub with a configured API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The runtime needs access to a Finnhub API key through an environment variable. <br>
Mitigation: Use a limited or revocable Finnhub key where possible and avoid storing the key in source files, logs, or shared command history. <br>
Risk: Fetching quotes contacts Finnhub and sends the requested ticker symbol to that service. <br>
Mitigation: Run the skill only in contexts where outbound requests to Finnhub and the associated data sharing are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/keyfrog-21k/skills/openclaw-finnhub) <br>
- [Finnhub](https://finnhub.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text quote output and Markdown usage guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.11+, finnhub-python, and a Finnhub API key in the finnhub_api_key environment variable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

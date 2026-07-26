## Description: <br>
Set up Brave Search API for OpenClaw web_search when a user needs to configure Brave API, get a Brave API key, enable web search, or fix a missing_brave_api_key error. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[garibong-labs](https://clawhub.ai/user/garibong-labs) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to configure Brave Search API access for web_search and repair missing Brave API key configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can reveal and store a live Brave API key without an explicit confirmation checkpoint. <br>
Mitigation: Invoke it only for explicit Brave API setup or missing-key repair, confirm the target config file before writing, and avoid exposing the full key in chat, logs, shell history, or process listings. <br>


## Reference(s): <br>
- [Brave Search API Dashboard](https://api-dashboard.search.brave.com) <br>
- [Brave Search API Keys](https://api-dashboard.search.brave.com/app/keys) <br>
- [ClawHub skill listing](https://clawhub.ai/garibong-labs/skills/brave-api-setup) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide an agent to write a Brave API key into the local OpenClaw configuration.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

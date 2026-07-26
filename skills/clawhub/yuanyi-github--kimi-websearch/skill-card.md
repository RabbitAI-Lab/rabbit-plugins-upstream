## Description: <br>
Kimi Websearch lets an agent submit natural-language search queries to RedFox/Kimi, poll for completion, and return structured web-search answers with citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuanyi-github](https://clawhub.ai/user/yuanyi-github) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Information seekers, content creators, researchers, and agents use this skill to retrieve current web-search answers from Kimi through RedFox for public, web-searchable questions that benefit from fresh information and cited sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to RedFox/Kimi using the configured RedFox API key. <br>
Mitigation: Use the skill only for public, web-searchable questions and avoid submitting private, internal, confidential, or sensitive text. <br>
Risk: The skill depends on a user-managed REDFOX_API_KEY. <br>
Mitigation: Store the key in an environment variable or secret manager, verify its source and revocation options, and never place it in prompts, logs, repositories, or output files. <br>
Risk: Live web-search results may be incomplete, stale, or require source verification. <br>
Mitigation: Review returned citations and source links before relying on results for decisions or publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yuanyi-github/skills/kimi-websearch) <br>
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=github) <br>
- [RedFoxHub](https://redfox.hk?source=github) <br>
- [English README](README.en.md) <br>
- [Kimi search script](scripts/kimi_search.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON results from the search helper script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided REDFOX_API_KEY; the helper script polls every 5 seconds for up to 5 minutes and prints final JSON to stdout.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

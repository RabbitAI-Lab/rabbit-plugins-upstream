## Description: <br>
DuckDuckGo and Wikipedia research CLI with URL fetching, readable text extraction, and citation-oriented output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, agents, and CI fact-checkers use this skill to run keyless web searches, Wikipedia lookups, and URL text extraction from a Python CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs external web requests for search, Wikipedia lookup, and user-specified URL fetches. <br>
Mitigation: Use it only where outbound web access is acceptable, avoid sensitive internal URLs, and review retrieved content before relying on it. <br>
Risk: Bundled CI verifier tooling can run local Python files when pointed at a folder. <br>
Mitigation: Do not run the verifier on untrusted folders unless isolated with no secrets, restricted network access, and disposable filesystem permissions. <br>


## Reference(s): <br>
- [ClawHub Web Research listing](https://clawhub.ai/itspremkumar/skills/web-research) <br>
- [DuckDuckGo Lite search endpoint](https://lite.duckduckgo.com/lite/) <br>
- [Wikipedia API endpoint](https://en.wikipedia.org/w/api.php) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Terminal text with optional saved text files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live web requests for search, Wikipedia, and URL fetches; fetch results can be written to a local text file.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

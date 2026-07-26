## Description: <br>
GEO brand optimization helps agents diagnose a brand's AI ecosystem presence, generate review articles, and submit generated content for publication through the Doubao-connected GEO API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chameleon-nexus](https://clawhub.ai/user/chameleon-nexus) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and brand operators use this skill to run brand visibility diagnostics across AI platforms, generate single-brand or comparison review articles, and check publication status through authenticated GEO API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit generated brand content for third-party publication without a separate human approval step. <br>
Mitigation: Confirm the brand, article type, comparison target, and publishing intent before running article generation or polling the generated article status. <br>
Risk: The skill requires a sensitive GEO API key and may save it in local key files. <br>
Mitigation: Use a limited API key where possible, protect local key files, and remove saved keys after use when persistent access is not needed. <br>
Risk: Frequent polling can trigger API rate limits. <br>
Mitigation: Respect the documented polling intervals and stop or delay retries after rate-limit responses. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chameleon-nexus/geo-brand-diagnosis) <br>
- [Publisher Profile](https://clawhub.ai/user/chameleon-nexus) <br>
- [GEO API Production Base URL](https://ai.gaobobo.cn) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and JSON API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided GEO API key and may write that key to local agent configuration files.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

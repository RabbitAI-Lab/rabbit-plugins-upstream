## Description: <br>
Browser Automation V2 Tool Free helps agents run lightweight single-page browser automation tasks such as opening pages, waiting for loads, extracting data, filling basic forms, retrying on timeouts, and cleaning up tabs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to automate lightweight single-page browsing workflows, including page loading, simple data extraction, basic form filling, timeout retries, and tab cleanup. It is best suited to user-directed URL tasks rather than sensitive login or high-volume scraping workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated login or password submission can expose credentials or submit sensitive forms without adequate safeguards. <br>
Mitigation: Avoid real logins and sensitive forms unless secure secret input, confirmation before submission, output redaction, and cleanup of logs, profiles, and generated files are in place. <br>
Risk: Local browser automation can interact with untrusted pages and persist browser state or generated outputs. <br>
Mitigation: Limit use to explicit user-directed URLs, review outputs before reuse, and clear browser profiles, logs, and generated files after the task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/browser-automation-v2-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, code snippets, YAML configuration examples, and JSON-style result examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe result objects with success, data, execution_log, and error fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

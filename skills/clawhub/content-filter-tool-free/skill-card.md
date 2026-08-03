## Description: <br>
This skill helps personal users configure keyword, regular-expression, author blocklist, whitelist, and local rule workflows for filtering noise from an information feed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to guide an agent through configuring and applying single-user feed filtering rules, including keywords, regex patterns, blocked authors, whitelisted authors, and review of filtered results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may require command execution, local rule-file writes, network access to a feed service, and an environment token. <br>
Mitigation: Review commands and file changes before execution, use least-privilege feed tokens, and confirm the service endpoint and transmitted data before providing credentials. <br>
Risk: The security summary says the mandatory LLM requirement is under-explained. <br>
Mitigation: Clarify what data is sent to the LLM and avoid using sensitive feed content until the LLM scope and safeguards are understood. <br>
Risk: Filtering rules can incorrectly hide useful feed items, especially broad regular expressions or blocklists. <br>
Mitigation: Use the documented blocked-item review and trace workflow, keep whitelist priority enabled for trusted authors, and narrow regex patterns after testing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/content-filter-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide local rule-file writes, network requests to a feed service, and use of an environment token.] <br>

## Skill Version(s): <br>
1.0.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Helps an agent configure and apply personal feed filters using keywords, regular expressions, author blocklists, whitelists, and local rule management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to manage single-user feed filtering rules, reduce feed noise, review filtered results, and tune false positives. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run commands, write local filtering rules, and use feed credentials while its execution scope and data handling are unclear. <br>
Mitigation: Review commands before execution, keep backups of filter-rules.json, use least-privilege feed tokens, and confirm whether feed content is sent to an LLM or external endpoint. <br>
Risk: Broad keyword or regular-expression rules can hide legitimate feed items. <br>
Mitigation: Start with narrow rules, use blocked-item review or trace output, and prefer whitelists for trusted authors. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/content-filter-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe local rule files, feed filtering commands, blocked-item review steps, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

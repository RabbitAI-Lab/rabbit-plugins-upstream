## Description: <br>
Generates and diagnoses Excel formulas from natural-language requests, including common functions such as VLOOKUP, SUMIF, and COUNTIF for individual daily spreadsheet tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and spreadsheet authors use this skill to turn plain-language spreadsheet needs into Excel formulas, diagnose formula errors, and simplify common formulas for personal daily use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad file write and command execution capability could alter local files or run commands during spreadsheet assistance. <br>
Mitigation: Install only when those permissions are acceptable, and review any command or file-changing action before allowing it. <br>
Risk: The optional callback_url can send results or related data to an external endpoint. <br>
Mitigation: Use callback_url only with endpoints you control and after confirming what data will be transmitted. <br>
Risk: Untrusted spreadsheet content or vague natural-language requests may lead to incorrect or unsafe formula guidance. <br>
Mitigation: Use trusted spreadsheet files, review generated formulas before applying them, and test changes on copies of important workbooks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/excel-formula-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Excel formula snippets, code examples, shell commands, configuration examples, and optional JSON-style structured results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include execution status, result data, execution logs, and error fields when presenting structured responses.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

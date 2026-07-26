## Description: <br>
Test and debug regular expressions with real-time matching, group extraction, and a common pattern library. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fuzzyb33s](https://clawhub.ai/user/fuzzyb33s) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to test, debug, validate, or explain regex patterns and inspect matches, capture groups, and JSON output from sample text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Extremely complex regexes or very large test strings can consume CPU during local Python regex evaluation. <br>
Mitigation: Use bounded sample inputs, avoid running untrusted expensive patterns on large text, and interrupt the local process if evaluation stalls. <br>
Risk: Sensitive text tested with the CLI is still local command input. <br>
Mitigation: Use sanitized samples when possible and avoid testing secrets or production data unless local handling is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fuzzyb33s/skills/regex-tester) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports match counts, match spans, capture groups, invalid regex errors, and common pattern names.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

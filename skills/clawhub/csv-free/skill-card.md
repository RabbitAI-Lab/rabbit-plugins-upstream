## Description: <br>
Csv Free helps agents parse and generate RFC 4180-style comma-separated CSV with basic quoting, escaping, empty-field handling, and column-count checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to format, parse, and validate simple CSV data for cross-tool exchange when comma delimiters and basic RFC 4180 quoting are sufficient. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan marked the release suspicious because the skill requests command execution and file-writing tools without a clear need for simple CSV formatting. <br>
Mitigation: Use it in a least-privileged agent session, review any proposed commands or file writes, and prefer a version that removes exec access or narrowly scopes writes. <br>
Risk: CSV contents can be mishandled by downstream tools because the free guidance does not include Excel formula-injection defenses, BOM handling, alternate delimiters, or detailed parse-failure diagnostics. <br>
Mitigation: Treat CSV contents strictly as data, validate outputs in the target tool, and avoid using this skill for workflows that require those protections. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/csv-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown responses with CSV text examples and validation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Limited to comma-separated RFC 4180-style CSV guidance; the free version does not cover BOM handling, alternate delimiters, Excel formula-injection defenses, or detailed parse diagnostics.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
JSON修复工具免费版 helps agents repair common JSON syntax problems such as trailing commas, single quotes, unquoted keys, JavaScript-style comments, and hexadecimal numbers while backing up and validating repaired files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, data analysts, and other technical users use this skill to repair malformed JSON files or snippets and receive a structured repair report. It is suited to configuration repair, log cleanup, hand-written JSON correction, third-party data cleanup, teaching examples, and migration data fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and modify JSON files in a workspace through agent command execution. <br>
Mitigation: Use explicit input and output paths, keep backups enabled, and review repaired files before relying on them. <br>
Risk: The security summary notes broad automatic triggers and unclear callback or network language. <br>
Mitigation: Install only if file-changing command access is acceptable, and avoid callback URLs unless the publisher clearly documents what will be sent and where. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/json-repair-tool-free) <br>
- [Source skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown instructions with JSON repair reports and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create repaired JSON files and .bak backups; repair reports include status, file paths, size changes, repair counts, validity, and success state.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

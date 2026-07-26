## Description: <br>
Content validation gateway free edition for AI application developers, providing basic AI-generated content policy checks, blocklist and allowlist management, content classification, and verification result logging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and individual AI application builders use this skill to perform basic content review before publishing or returning AI-generated output. It helps manage local policy terms, classify sensitive content, filter blocked terms, and record verification outcomes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist content previews or other sensitive snippets in local verification logs. <br>
Mitigation: Avoid logging raw prompts, credentials, personal data, or regulated content unless the logging example is modified to redact or omit previews. <br>
Risk: The release has an unresolved callback_url field while also claiming local-only handling. <br>
Mitigation: Treat callback behavior as unresolved and review any network-related use before deploying the skill in workflows that process sensitive data. <br>
Risk: The skill relies on command execution and local file writes for rule, output, and log management. <br>
Mitigation: Run it only in an appropriate workspace, review proposed commands before execution, and limit write access to intended rule, output, and log locations. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with Python and bash code blocks, JSON-shaped result examples, and local file path conventions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local rule, filtered-output, and verification log files when the suggested commands are executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

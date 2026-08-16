## Description:

JSON验证工具 helps agents validate JSON syntax and structure through an Expanso Edge workflow for automation and integration tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation teams use this skill to check JSON syntax and structure before using JSON in API integrations, data synchronization, and workflow automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests command execution and file writing in broad, under-scoped instructions.

Mitigation: Run it in a sandbox, grant only task-scoped filesystem access, and confirm any command execution or file write before allowing it.

Risk: API-backed JSON validation can expose sensitive JSON content if the user submits secrets or private data.

Mitigation: Avoid sensitive JSON, redact secrets before validation, and confirm any API call before sending data outside the local agent environment.

Risk: Validation guidance or generated results may be incorrect or misleading.

Mitigation: Review the validation result before acting on it, especially when the JSON affects production systems or automated workflows.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON result examples and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request JSON content, processing mode, retry count, skipped steps, and API-key-backed execution.]

## Skill Version(s):

1.0.1 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

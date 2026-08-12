## Description:

Searches local Windows files and folders with the bundled Everything engine, supporting name, size, date, type, regular-expression, and content filters with structured JSON results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kiwifruit13](https://clawhub.ai/user/kiwifruit13)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to locate files on Windows systems, narrow searches with Everything query syntax, and return file paths and metadata for further agent work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run bundled Windows search binaries and broadly index or expose local file metadata.

Mitigation: Install only in environments where that local file metadata exposure is acceptable, and prefer an already trusted local Everything installation when available.

Risk: Content searches can inspect sensitive locations if the user asks for them and content indexing is enabled.

Mitigation: Avoid content searches on sensitive paths unless the user explicitly intends those contents to be searched.

Risk: The bundled Everything instance may remain running after use.

Mitigation: Review the running Everything process after use and stop it if persistent local indexing is not desired.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results include query, engine, total, returned, warning, and result objects with path, name, folder flag, size, and modified date.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

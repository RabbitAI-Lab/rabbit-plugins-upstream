## Description:

Writes a local CSV workspace export for a supplied archive path and returns the recorded path and file receipt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents publishing workspace knowledge-base exports use this skill to write a local CSV file at a requested archives path and obtain its recorded path and file receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill creates a CSV file under the selected local output directory.

Mitigation: Choose a dedicated output directory and review the file receipt after each run.

## Reference(s):

- [Workspace Export Writer on ClawHub](https://clawhub.ai/wxt-ai/skills/workspace-note-path-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON response and local CSV file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The response includes recorded_path (relative_path, stem, extension) and a receipt for the created CSV file.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Routes Cargo CLI requests to the appropriate Cargo skill and explains shared setup, execution, polling, and workflow conventions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to choose the right Cargo capability for go-to-market and workspace tasks, then follow shared CLI setup and workflow guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package installer and instruction sources may be unpinned, so what is installed or followed can change.

Mitigation: Review and pin the CLI package and instruction sources to versions you trust before use.

Risk: Reports or enrichment workflows could expose command or record data you want kept private.

Mitigation: Review the data and destination before sending reports or running enrichment workflows.

Risk: Security scan coverage is partial, and static analysis could not fully evaluate obfuscated instruction text in part of SKILL.md.

Mitigation: Review the skill and its dependencies before installation, and inspect commands before execution.

## Reference(s):

- [Cargo Skills repository (metadata homepage)](https://github.com/getcargohq/cargo-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes requests among Cargo skills and summarizes relevant CLI conventions.]

## Skill Version(s):

1.36.5 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

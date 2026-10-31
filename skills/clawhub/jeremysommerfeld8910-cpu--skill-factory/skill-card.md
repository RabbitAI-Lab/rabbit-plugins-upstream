## Description:

Create, evaluate, improve, benchmark, and publish OpenClaw skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeremysommerfeld8910-cpu](https://clawhub.ai/user/jeremysommerfeld8910-cpu)

### License/Terms of Use:


## Use Case:

Developers and skill authors use this skill to create new OpenClaw skills, evaluate and improve existing skills, compare versions, analyze reusable patterns, and package skills for publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad local skill scans can expose file names, tool usage, or patterns from installed skills.

Mitigation: Review scan directories before running pattern analysis and limit scans to verified skill directories.

Risk: Packaging workflows can include unintended files in a published skill archive.

Mitigation: Inspect the full package manifest and generated .skill archive contents before publishing.

Risk: Generated pattern reports or eval results can carry untrusted or low-quality guidance into future skill edits.

Mitigation: Keep generated reports as review inputs and require human approval before rewriting or publishing skills.

Risk: Fallback commands that locate helper scripts through filesystem search can select an unexpected installation path.

Mitigation: Run bundled scripts only from a verified skill installation path.

## Reference(s):

- [OpenClaw Skill Patterns](references/patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash, JSON, and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify skill files, eval reports, pattern reports, and packaged .skill archives when directed by the user.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

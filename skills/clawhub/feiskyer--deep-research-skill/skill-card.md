## Description:

Deep Research orchestrates multi-agent research by decomposing a research goal into parallel Claude Code subprocesses, collecting web or file evidence, aggregating child reports, and delivering a polished report file with key findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[feiskyer](https://clawhub.ai/user/feiskyer)

### License/Terms of Use:


## Use Case:

Developers, analysts, and research teams use this skill to plan and run systematic deep-research workflows for web or document research, competitive and industry analysis, bulk retrieval, and long-form evidence-integrated reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spawn multiple Claude Code subprocesses with shell, file, and network-capable tools.

Mitigation: Require an explicit execution plan before running, restrict child-agent tools and workspace paths, and avoid use on sensitive repositories or private data unless the scope is approved.

Risk: The security evidence flags unsafe shell scheduling examples and possible shell interpolation issues.

Mitigation: Validate task IDs and other scheduler inputs, avoid interpolating untrusted values into shell commands, and review dispatch scripts before execution.

Risk: The workflow can create .research files and use search or scraping tools during data collection.

Mitigation: Constrain network targets and data-retention locations, keep logs for traceability, and review generated reports before relying on conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/feiskyer/skills/deep-research-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, shell command snippets, configuration instructions, and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are expected to be saved as files, with intermediate logs and raw materials retained under a .research directory.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps agents measure Cargo workflow runs and export run, batch, and segment data using the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to check workflow success and error counts, download run and batch outputs, and export Cargo segment data for analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exports may disclose sensitive Cargo workspace data or signed download URLs.

Mitigation: Limit workflow, batch, date, record count, and fields; handle signed URLs and downloaded files as sensitive.

Risk: Installing an unvetted or changing CLI package may expose the workspace.

Mitigation: Install only from a trusted package source and prefer a pinned, vetted CLI version over @latest.

Risk: Re-running failed records or creating a batch can change workspace data and incur costs.

Mitigation: Confirm the selected workspace and obtain approval before any rerun or batch creation.

## Reference(s):

- [Cargo Analytics skill page](https://clawhub.ai/cargo-ai/skills/cargo-analytics)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Data export examples](references/examples/exports.md)
- [Run analytics examples](references/examples/run-analytics.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Analysis]

**Output Format:** [Markdown with CLI commands and summaries of JSON results or export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downloads may return signed URLs to CSV or JSON files rather than file contents.]

## Skill Version(s):

1.7.0 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

CSV Inspect previews CSV and TSV files before analysis by reporting column names, encoding, delimiter, row count, inferred types, and first or last rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alex-ht](https://clawhub.ai/user/alex-ht)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data analysts, and agents use this skill to inspect delimited text files before parsing, analysis, or pandas work. It is intended for schema, header, delimiter, encoding, row count, type, and small sample previews rather than statistical reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Preview output can expose real cell values from local CSV or TSV files.

Mitigation: Avoid running the skill on regulated, secret, or otherwise sensitive data unless transcript and output storage are acceptable.

Risk: Delimiter or type inference can be wrong for tiny or unusual files.

Mitigation: Use the reported delimiter and encoding in later parsing, and re-run with a larger sample or explicit delimiter when the output indicates suspicious single-column parsing.

Risk: The skill depends on the csv-inspect executable being available on PATH.

Mitigation: Confirm the installed command is on PATH before use and invoke csv-inspect directly rather than calling the bundled script path.

## Reference(s):

- [CSV Inspect ClawHub listing](https://clawhub.ai/alex-ht/skills/csv-inspect)
- [Publisher profile](https://clawhub.ai/user/alex-ht)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON inspection results, usually relayed or summarized in Markdown with shell command invocations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default preview is five head rows, zero tail rows, and type inference from the first 200 data rows; output can include sampled cell values.]

## Skill Version(s):

1.2.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

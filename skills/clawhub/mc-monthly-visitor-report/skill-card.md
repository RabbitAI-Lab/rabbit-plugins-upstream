## Description:

Uses ideamake-cli to pull marketing-cloud data and generate an end-to-end monthly real-estate visitor analysis report in HTML and PDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crespoyin](https://clawhub.ai/user/crespoyin)

### License/Terms of Use:

MIT-0

## Use Case:

Real-estate marketing and sales operations teams use this skill to fetch project, customer, and recorded reception transcript data, analyze monthly visitor behavior and sales conversion signals, and produce management-ready HTML and PDF reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow bulk-downloads and stores customer recordings, transcripts, identifiers, and sales reports.

Mitigation: Run it only with explicit authorization, store outputs in controlled locations, restrict report sharing, and apply retention or deletion rules to local artifacts.

Risk: Customer names, phone-number fragments, and transcript-derived content can appear in generated filenames and reports.

Mitigation: Use redacted filenames where possible and review generated reports for unnecessary personal or sensitive data before distribution.

Risk: The analysis may produce operational sales recommendations from sensitive transcript data.

Mitigation: Have authorized business reviewers validate recommendations against source data before using them for performance decisions or external reporting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crespoyin/skills/mc-monthly-visitor-report)
- [Publisher profile](https://clawhub.ai/user/crespoyin)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Analysis, Guidance]

**Output Format:** [Markdown instructions with shell commands, generated Markdown data files, HTML report, transcript text files, and PDF report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authenticated ideamake-cli access and a onepage-pdf conversion workflow.]

## Skill Version(s):

0.2.0 (source: server release metadata; artifact frontmatter metadata.version is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

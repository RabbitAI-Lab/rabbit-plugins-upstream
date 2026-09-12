## Description:

Analyzes batches of Douyin, Xiaohongshu, and Bilibili video links by using qhkit to fetch engagement metrics and export an Excel spreadsheet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and social media operators use this skill to batch-check short-video performance metrics, compare owned or competitor videos, and obtain an exported data table for follow-up analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or upgrades an unpinned third-party command-line tool that handles API tokens and submitted video links.

Mitigation: Review @iqinghu/qhkit before installation, prefer a pinned local package version, and verify package integrity before use.

Risk: The workflow can submit paid jobs and may expose submitted video links to the Qinghu service.

Mitigation: Run the estimate step before generation, confirm credit cost with the user, use trusted tokens, and avoid submitting links the user is not authorized to process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shortvideo-data-engine)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples; completed runs may return xlsx file URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses qhkit workflow actions for options, estimate, generate, and status polling; submitted jobs can consume Qinghu credits.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

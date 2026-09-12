## Description:

This skill helps agents use Qinghu's qhkit workflow to collect creator profile metrics from Douyin, Xiaohongshu, and Bilibili homepages and export the results as an Excel spreadsheet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, creator-operations, and competitive-intelligence users can ask an agent to submit up to five supported creator homepage links, estimate cost, run the Qinghu workflow, poll for completion, and return the exported account-data spreadsheet. The skill is intended for one-time data pulls; scheduled updates are configured in the Qinghu workbench.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade an unpinned global npm CLI and write long-lived Qinghu credentials.

Mitigation: Use a pinned, reviewed qhkit version in an isolated environment and provide a scoped token through an environment variable or controlled config path.

Risk: Workflow runs can consume paid credits and process creator data supplied by the user.

Mitigation: Run estimate with the final parameters, confirm cost before generation, and submit only supported creator homepage links the user is authorized to process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-creator-data-engine)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline bash commands and JSON snippets; completed runs return XLSX file links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Submits Qinghu workflow wf_052, polls by logId, and reports final credit consumption when a task completes.]

## Skill Version(s):

0.1.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

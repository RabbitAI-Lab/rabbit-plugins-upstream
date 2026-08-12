## Description:

Cue 深研 lets an agent route public-data research questions to Cue buddy templates or free-form deep research, confirm credit use, run jobs in the background, and return sourced Markdown reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers use this skill to run Cue-backed public-data research from a chat workflow, choose from matching saved templates or free-form research, and receive a cited report. It is intended for public-source business, investment, compliance, and industry research rather than private AML, medical, internal accounting, or confidential-document workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, research context, and selected files may be sent to Cue's backend.

Mitigation: Use the skill only for data you are comfortable sending to Cue, and avoid private AML, medical, internal accounting, confidential contracts, or other sensitive documents unless Cue's handling has been reviewed.

Risk: Local sample or material files can be uploaded for mimic or document-grounded research.

Mitigation: Upload files only after explicit user confirmation, and treat server limits and retention/handling policies as review items before sensitive use.

Risk: The skill includes update behavior that can check or upgrade from a remote branch.

Mitigation: Review the update behavior before allowing +upgrade or silent update checks in managed environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-research)
- [Cue API endpoint](https://cuecue.cn/api)
- [Cue API key page](https://cuecue.cn/api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with inline links, short user prompts, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs can write reports and progress logs to local files; optional material or mimic files may be uploaded to Cue after user confirmation.]

## Skill Version(s):

1.0.1 (source: server release metadata); artifact metadata version 0.3.4

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

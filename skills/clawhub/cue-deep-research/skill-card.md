## Description:

Cue 深度研究（通用版） helps agents run public-information financial, business, industry, competitor, and compliance research through Cue, producing sourced Markdown reports with cross-checked findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask financial, commercial, industry, competitor, and public-risk research questions and receive structured Markdown reports with source links. It is suited to public-market research, competitor comparison, investment pre-checks, industry trend analysis, compliance screening, and style-matched report drafting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries are sent to the Cue service and may describe sensitive research interests.

Mitigation: Confirm trust in the Cue service before installation and avoid submitting confidential, personal, regulated, or proprietary research topics.

Risk: Using --mimic-file uploads the selected local document to Cue for style analysis.

Mitigation: Do not use --mimic-file with confidential, personal, regulated, or proprietary documents.

Risk: Reports are written to a local output folder selected by the user.

Mitigation: Choose an output folder appropriate for the sensitivity of the research topic and resulting report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-deep-research)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API key page](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown report with source links, plus shell commands and configuration guidance for running Cue.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are saved to a user-selected local output path; optional mimic inputs can guide writing style.]

## Skill Version(s):

1.0.6 (source: server release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

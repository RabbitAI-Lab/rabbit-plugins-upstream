## Description:

疑难法律实操案例库围绕一个法律争议点检索公开裁判文书、监管问答与实务案例，并归纳裁判要点、争议焦点与可落地的实操口径。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Legal and compliance practitioners use this skill to research Chinese legal practice questions, compare public case outcomes and regulatory positions, and produce a source-linked reference report. It is intended as research support and does not replace professional legal judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and the Cue API key are used with an external Cue service.

Mitigation: Use a dedicated Cue API key, store it only in the expected local configuration, and run the documented health check before research.

Risk: Each research run may consume Cue credits.

Mitigation: Confirm credit availability and expected cost before running; the artifact estimates about 3-8 credits per research request.

Risk: Legal research output may be incomplete, outdated, or unsuitable as legal advice.

Mitigation: Verify conclusions against the cited case numbers and source links, and have qualified legal professionals review any decision-critical use.

Risk: Cue service availability and public data source coverage can affect report completeness.

Mitigation: Run the documented service and playbook checks first, retry after service interruptions, and use listed public-source fallback channels when Cue is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-legal-practice-cases)
- [Publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue playbook source](https://cuecue.cn/playbook)
- [Cue API key](https://cuecue.cn/api-key)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese Markdown report with cited case numbers and source links, plus setup and diagnostic shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are written to a local Markdown file under ~/cue-reports and can optionally be converted to DOCX or PDF with pandoc.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

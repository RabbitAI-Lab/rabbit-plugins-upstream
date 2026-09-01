## Description:

ClawVision turns an OpenClaw chat session into tabbed HTML, PNG, Markdown, and PowerPoint summaries with optional session analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monaxamo](https://clawhub.ai/user/monaxamo)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to create exportable visual summaries of OpenClaw sessions after confirming the session is appropriate to export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads session history and writes export files that may contain session-derived content.

Mitigation: Use it only for sessions that are safe to export, avoid sessions with secrets or private identifiers, and inspect generated files before sharing.

Risk: Analytics rendering may load ECharts from a CDN when the local bundle is absent.

Mitigation: Treat chart generation as network-enabled unless ECharts is vendored locally or analytics chart generation is disabled.

## Reference(s):

- [ClawVision homepage](https://github.com/monaxamo/clawvision)
- [ClawHub skill page](https://clawhub.ai/monaxamo/skills/clawvision)
- [ECharts CDN fallback](https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Export files including HTML, PNG screenshots, Markdown summaries, PowerPoint decks, and optional analytics chart artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated outputs are written to disk and may include session-derived content.]

## Skill Version(s):

1.0.11 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

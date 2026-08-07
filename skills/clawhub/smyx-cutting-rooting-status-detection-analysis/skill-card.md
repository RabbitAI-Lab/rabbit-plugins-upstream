## Description:

Analyzes images or videos of plant cuttings in transparent containers to detect visible root primordia and rooting stage, then returns a structured rooting-status report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, propagators, and plant-research users can use this skill to assess cutting-rooting progress from transparent-container images or videos. It reports rooting stage, root-point count and distribution, approximate early-root length, transplant timing guidance, and cloud report links or history when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided plant images, videos, or URLs are sent to external lifeemergence/open.lifeemergence cloud services for analysis and report history.

Mitigation: Review data-sharing requirements before installation and avoid submitting sensitive images, private URLs, or media that should not leave the workspace.

Risk: The skill creates or reuses an internal identity and may store service tokens in a local workspace database.

Mitigation: Run it in a controlled workspace, inspect local storage after use, and clarify identity and token handling with the publisher before broad deployment.

Risk: The bundled API reference still describes pet-health endpoints while the skill presents plant rooting analysis behavior.

Mitigation: Confirm the publisher's current API contract and expected scene code before relying on reports in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cutting-rooting-status-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface reference](artifact/references/api_doc.md)
- [Shared analysis API reference](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON structured report with report links and optional history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local file paths or public media URLs; documented supported formats are jpg, png, mp4, avi, and mov with a 10 MB limit.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

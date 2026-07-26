## Description: <br>
Analyzes child study-area video from a smart desk lamp or tabletop camera to estimate focus scores, identify distraction periods, and return structured study-behavior reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit a child study-area video or URL and receive visual focus metrics, distraction-event summaries, historical report listings, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Child study videos, URLs, and identifiers may be processed by the vendor's cloud service. <br>
Mitigation: Use only with appropriate guardian consent, and confirm the vendor's retention, deletion, and access-control practices before submitting sensitive child media. <br>
Risk: The skill may silently create or reuse a local identity and cache service tokens in a workspace SQLite database. <br>
Mitigation: Prefer a version that asks for explicit consent before uploads or identity creation, and inspect and remove stored identity or token data after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-focus-analysis-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files] <br>
**Output Format:** [Markdown or JSON analysis output, with optional saved result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [History report lists are rendered as Markdown tables; analysis results may include focus scores, distraction events, alerts, and report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

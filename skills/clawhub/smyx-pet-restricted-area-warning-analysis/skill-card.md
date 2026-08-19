## Description:

Monitors restricted area intrusions, climbing on dining tables, and rummaging through trash cans, and issues real-time alerts for home pet monitoring scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and home-monitoring operators use this skill to analyze pet monitoring videos or URLs for restricted-zone entry, table climbing, trash rummaging, and related alert reports. Agents can also use it to query the user's cloud report history when the user asks for prior pet restricted-area warning reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-monitoring media or media URLs are sent to cloud services for analysis and report history retrieval.

Mitigation: Install and run only when the publisher and cloud processing path are acceptable for the user's household monitoring content.

Risk: The skill silently derives or creates an account identity and stores authentication tokens in a workspace database.

Mitigation: Review workspace persistence and token handling before deployment, and remove stored account state when the skill is no longer trusted or needed.

Risk: The security verdict is suspicious because cloud-backed analysis and persistent account state are used.

Mitigation: Review the ClawHub security summary and guidance before installation, and monitor network use during execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-restricted-area-warning-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and JSON analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include alert summaries, structured detection details, cloud report links, and optional saved output files.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

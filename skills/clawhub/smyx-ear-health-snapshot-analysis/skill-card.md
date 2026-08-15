## Description:

Analyzes pet ear images or videos to identify visible ear-canal redness, discharge, earwax buildup, and related abnormality alerts without providing a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, boarding centers, and veterinary pre-screening teams use this skill to turn pet ear media into structured visual observations, risk prompts, recommendations, and report links. It can also retrieve cloud-hosted history for prior ear-health analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media or video URLs are sent to lifeemergence.com services for analysis.

Mitigation: Use only media appropriate for remote processing, disclose the external service dependency, and avoid submitting sensitive or unrelated recordings.

Risk: The skill can create or reuse backend identity, store backend tokens locally, and retrieve cloud history without explicit per-use confirmation.

Mitigation: Review authentication and retention behavior before installation, clear local workspace credentials when no longer needed, and prefer versions that expose identity, deletion, and history lookup controls.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON/plain text reports emitted by shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured observations, abnormality alerts, recommendations, report links, and optional saved output files.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter lists 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

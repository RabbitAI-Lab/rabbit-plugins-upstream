## Description:

Analyzes pet race start and finish video to identify start timing, lane assignment, finish order, false starts, and lane-crossing fouls for referee review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, event operators, and developers use this skill to submit pet race video or video URLs and receive structured referee-support results for false-start and lane-crossing review. The outputs are intended to support human adjudication, not replace the final decision of race officials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Race videos or video URLs are sent to the configured cloud service for analysis.

Mitigation: Use non-sensitive media, confirm publisher retention and processing terms, and avoid submitting confidential footage unless those controls are acceptable.

Risk: The skill may silently create or reuse an internal identity and tie history reports to that identity.

Mitigation: Run the skill in a dedicated workspace and review account scoping before using history-report features.

Risk: Service tokens may be stored in a local workspace database.

Mitigation: Restrict local workspace access, avoid shared workspaces for sensitive use, and clear local data when the skill is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-race-foul-detection-analysis)
- [API Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Structured text or Markdown containing JSON-like analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include saved output files when the optional output path is provided.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

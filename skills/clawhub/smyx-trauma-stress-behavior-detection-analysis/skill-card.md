## Description:

Analyzes fixed-camera emergency shelter video to identify visual behavior signals associated with acute stress, generate psychological crisis alerts, and guide authorized on-site responders toward human-reviewed support actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Emergency-response operators and authorized psychological-rescue teams use this skill to triage fixed-camera shelter footage for visual behavior observations, location markers, crisis alert levels, PFA-oriented response guidance, and historical report lookup. It is intended to support human-reviewed field response, not clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly sensitive emergency-scene footage and behavior observations.

Mitigation: Deploy only in controlled emergency-response environments with documented legal authority, role-based access, retention limits, and face-blurring or other required privacy protections.

Risk: Cloud upload and cloud history lookup can expose sensitive reports or personal context if used without operator awareness.

Mitigation: Require explicit operator approval for cloud processing and history retrieval, and limit access to authorized emergency-command or licensed psychological-rescue personnel.

Risk: Behavior alerts could be mistaken for clinical mental-health diagnoses or automatic dispatch decisions.

Mitigation: Treat outputs as triage signals only; require human review before escalating high-risk alerts and route interventions through qualified responders.

Risk: Persistent identity, token, or profile data may remain on local storage.

Mitigation: Define a plan for clearing local SQLite token and profile data, and enforce retention and access controls on the deployment host.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-trauma-stress-behavior-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis reports with crisis alert levels, behavior observations, response guidance, report links, and optional saved files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud-hosted history reports and may write an output file when requested.]

## Skill Version(s):

1.0.12 (source: server release metadata and target metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Identifies bird species in images/videos of target areas, supports recognition of no less than 500 common bird species, and supports customized model training for ecological observation, garden bird watching, and related scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to identify bird species from image, video, or URL inputs and receive structured recognition results, confidence-oriented findings, recommendations, and report links. It also supports querying previously generated cloud reports associated with the current skill identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded images, videos, and provided URLs are sent to lifeemergence.com services for analysis.

Mitigation: Use the skill only with media that is appropriate to send to that external service, and avoid confidential or regulated content unless the deployment has approved that data flow.

Risk: The skill silently creates or reuses an identity and associates analysis and report-history requests with it.

Mitigation: Review the identity behavior before installation and run the skill only in workspaces where automatic identity association is acceptable.

Risk: Service tokens can be stored locally in SQLite for later API calls.

Mitigation: Limit filesystem access to the workspace, rotate tokens if the workspace is shared or compromised, and remove local token storage when decommissioning the skill.

Risk: Cloud report-history queries may return records associated with the current identity.

Mitigation: Confirm that users invoking history queries are authorized to view reports linked to that identity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-bird-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Bird recognition API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration]

**Output Format:** [Markdown or JSON text containing structured bird-recognition results, report records, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can optionally write the returned report content to a user-specified output file.]

## Skill Version(s):

1.0.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

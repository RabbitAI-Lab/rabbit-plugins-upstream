## Description:

Real-time detection of flames and smoke in video and image scenes, suitable for fire early warning in industrial parks, forests, warehouses, and other locations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and safety operations teams use this skill to analyze uploaded or URL-provided images and videos for fire and smoke indicators, including flame detection, smoke recognition, location marking, confidence assessment, severity judgment, and report history lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded files, URL-provided media, identity data, and report-history requests are sent to lifeemergence.com or open.lifeemergence.com services.

Mitigation: Use the skill only with media that is authorized for third-party cloud processing, and avoid sensitive surveillance footage unless that data sharing is accepted.

Risk: The skill can create or reuse local user identity state, read data/smyx-api-key.txt if present, and store service tokens locally.

Mitigation: Run it in an isolated workspace, restrict access to the workspace data directory, and remove local identity or token files when they are no longer needed.

Risk: The detection output is an automated safety signal and may be incomplete or incorrect for emergency response decisions.

Mitigation: Treat results as warning support only, confirm suspected fires through established safety procedures, and contact emergency services when fire is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fire-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON text containing structured fire and smoke analysis, recommendations, report links, or report-history tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the returned report text to a user-selected output file when the --output option is used.]

## Skill Version(s):

1.0.16 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

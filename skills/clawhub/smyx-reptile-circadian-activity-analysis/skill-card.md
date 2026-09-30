## Description:

Analyzes fixed-camera reptile enclosure video to quantify 24-hour activity patterns, compare them with species circadian expectations, and produce structured rhythm reports with alerts and care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and reptile keepers use this skill to analyze enclosure video or report history for hourly motion, peak activity periods, rhythm consistency, and non-diagnostic husbandry guidance. It is intended for reptile enclosures, vivaria, breeding operations, and observation workflows that need structured day/night activity reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reptile enclosure media and report history are processed by lifeemergence.com services.

Mitigation: Install only when this cloud processing is acceptable for the workspace and intended users.

Risk: The skill silently creates or reuses an identity and stores service tokens locally.

Mitigation: Review or clear the workspace data store if persisted service tokens or default user records are not desired.

Risk: The skill can provide husbandry guidance based on video-derived activity patterns.

Mitigation: Keep outputs non-diagnostic and review recommendations before acting, especially when persistent abnormalities or health signs are present.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-circadian-activity-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include hourly activity arrays, peak and quiet hours, light/dark activity ratios, rhythm consistency scores, alert levels, recommended actions, disclaimers, and report links.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

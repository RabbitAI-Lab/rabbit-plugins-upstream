## Description:

Identifies obesity, emaciation, external injuries, skin abnormalities, and abnormal mental states in pet images or videos, helping pet owners detect possible health issues promptly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners and agent users can use this skill to analyze pet photos, videos, or media URLs for body condition, skin abnormalities, injuries, mental state indicators, and prior cloud report history. Its findings are health-reference guidance and do not replace professional veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media or media URLs are sent to an external service for cloud processing.

Mitigation: Install and run the skill only when the publisher and external processing are acceptable for the media being analyzed.

Risk: The skill silently creates or reuses an account-linked identity and may store local account tokens.

Mitigation: Run in an isolated workspace when evaluating the skill and review or clear persisted account data according to the host environment's policy.

Risk: Evidence reports that the current configuration selects private non-HTTPS development endpoints.

Mitigation: Confirm the intended production HTTPS configuration before use and avoid sending sensitive media through private HTTP endpoints.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-body-health-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with findings, suggestions, report links, and optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports image or video inputs from local files or URLs, history-list output, and basic, standard, or JSON detail levels.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

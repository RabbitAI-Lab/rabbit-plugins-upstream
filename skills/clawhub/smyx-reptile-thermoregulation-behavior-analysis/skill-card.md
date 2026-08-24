## Description:

Analyzes fixed-camera reptile enclosure videos to report basking, hiding, cool-zone dwell time, movement frequency, activity rhythm, and thermal preference signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, reptile keepers, breeders, and developers can use this skill to analyze enclosure camera video or URLs for thermal-zone utilization reports and behavior-based husbandry guidance. The output is informational and should be checked against on-site observations and professional veterinary advice for health concerns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends video files or video URLs and identity-linked request data to configured cloud services.

Mitigation: Use only with videos the user is authorized to submit, verify the configured service endpoints before execution, and avoid submitting sensitive enclosure footage unless the publisher and service are trusted.

Risk: The skill may create or reuse an identity and persist authentication tokens locally.

Mitigation: Run it in a controlled workspace, review local credential storage expectations before installation, and clear persisted identity or token data when the workspace is no longer trusted.

Risk: Behavior reports can influence animal-care decisions even though the skill does not provide a veterinary diagnosis.

Mitigation: Treat findings as behavior-analysis guidance, confirm camera coverage and device state, and escalate concerning or persistent alerts to a qualified reptile veterinarian.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-thermoregulation-behavior-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured text; optional saved text output when an output path is provided.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include thermal-zone ratios, transition counts, rhythm scores, preference labels, alert levels, recommended actions, disclaimers, and report links.]

## Skill Version(s):

1.0.8 (source: server release evidence; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

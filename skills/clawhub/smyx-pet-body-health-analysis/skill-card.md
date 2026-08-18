## Description:

Identifies obesity, emaciation, external injuries, skin abnormalities, and abnormal mental states in pet images or videos, helping pet owners detect possible health issues promptly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners and agents use this skill to submit pet images, videos, or media URLs for body condition and health analysis, including obesity, emaciation, injury, skin abnormality, and mental-state indicators. The skill can also retrieve account-linked historical analysis reports from the configured cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media and account-linked identifiers are sent to remote services for analysis and historical report retrieval.

Mitigation: Review the remote service and data-handling terms before installation, and avoid submitting sensitive media unless the deployment is approved for that data.

Risk: The skill can create or reuse a backend identity and store tokens in a local SQLite database.

Mitigation: Run the skill in a protected workspace, limit file access to the agent data directory, and rotate or remove stored tokens when access is no longer needed.

Risk: Packaged configuration includes HTTP development endpoints even though the documentation describes HTTPS transfer.

Mitigation: Confirm production configuration uses approved HTTPS endpoints before execution and do not use development endpoint settings for normal releases.

Risk: Health analysis results may be mistaken for a professional veterinary diagnosis.

Mitigation: Present results as screening guidance only and direct users to consult a veterinarian for abnormal findings or medical decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-body-health-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration]

**Output Format:** [Markdown or JSON analysis report with optional saved text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include health findings, suggestions, report identifiers, and report links returned by the remote service.]

## Skill Version(s):

1.0.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes reptile enclosure images or videos to classify shedding progress, identify stuck-shed risk areas, and produce care recommendations with report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, breeders, enclosure operators, and developers use this skill to analyze fixed-camera media for shedding phase, blue-eye signals, stuck-shed warning areas, image quality, and follow-up care guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet enclosure media or media URLs may leave the device for backend analysis.

Mitigation: Use only media appropriate for the configured backend, verify the service endpoint before running, and avoid submitting sensitive or unnecessary footage.

Risk: The skill may create or reuse an internal identity and store account tokens in a local SQLite database.

Mitigation: Install in a controlled workspace, restrict access to the local data directory, and review token storage and cleanup practices before shared or production use.

Risk: Security evidence reports development network endpoint defaults and limited user control over backend selection.

Mitigation: Confirm the configured API endpoints match the intended environment before execution and avoid running the skill against unknown or development services.

Risk: The skill provides animal-care recommendations that could be mistaken for veterinary diagnosis.

Mitigation: Treat output as visual assessment guidance, preserve the skill's no-diagnosis and no-invasive-action boundaries, and escalate persistent or severe stuck-shed findings to a qualified reptile veterinarian.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-shedding-progress-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or JSON analysis report with command-line execution guidance and optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include shedding phase, observed visual signals, stuck-shed risk areas, recommended actions, disclaimers, and report export links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

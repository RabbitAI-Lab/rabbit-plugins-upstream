## Description:

Analyzes reptile enclosure images or videos to classify shedding phase, detect visible stuck-shed risk signals, and return care-oriented monitoring guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, breeders, enclosure-system operators, and agents use this skill to analyze reptile full-body media, monitor shedding progress, identify visual warning signs such as retained skin around high-risk areas, and produce non-diagnostic care recommendations. It supports current analysis and cloud-backed history/report lookup for the same shedding-monitoring workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reptile images, videos, and remote media URLs may be sent to the LifeEmergence cloud service for analysis and report history.

Mitigation: Use only with media that users are allowed to submit to the cloud service, disclose the cloud-processing dependency, and avoid inputs that require local-only handling.

Risk: The skill can automatically use or create an internal identity and persist local tokens for cloud access.

Mitigation: Review the account bootstrap and local credential storage behavior before deployment; disable or replace it when explicit identity control, managed credentials, or local-only execution is required.

Risk: Animal-care guidance from visual analysis could be mistaken for veterinary diagnosis or treatment instructions.

Mitigation: Present outputs as advisory visual monitoring only, keep medication and invasive procedure advice out of responses, and direct persistent or severe stuck-shed concerns to a qualified reptile veterinarian.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-reptile-shedding-progress-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON analysis fields, status messages, history records, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local image/video files or remote media URLs; may return current analysis results, history listings, and exported report links.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

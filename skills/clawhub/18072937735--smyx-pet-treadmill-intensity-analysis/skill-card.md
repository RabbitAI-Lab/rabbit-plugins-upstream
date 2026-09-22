## Description:

Analyzes pet treadmill videos, optionally with heart-rate band data, to estimate stride frequency, limb extension, respiratory rate, exercise intensity, and pacing suggestions for dogs and cats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, smart treadmill vendors, training centers, and rehabilitation staff use this skill to assess pet exercise load from treadmill video and optional heart-rate data. The output supports training and pacing decisions, not medical diagnosis or treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos, report history identifiers, and username or phone-style open-id values may be sent to Life Emergence cloud services.

Mitigation: Install and run only when this data transfer is acceptable; avoid shared workspaces unless token storage and retention are approved.

Risk: The skill is framed as pet treadmill analysis, but server evidence describes broad cloud analysis and account behavior with under-disclosed token storage.

Mitigation: Review the skill before installing, confirm cloud endpoints and account behavior, and do not place real API secrets in fields treated as identity.

Risk: Exercise intensity output could be mistaken for veterinary guidance.

Mitigation: Use results only for training and pacing support, and rely on veterinary professionals for diagnosis, treatment, or safety-critical decisions.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-treadmill-intensity-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured reports, with shell command examples for invoking API-backed analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis output to a requested file and can present history results as a Markdown table.]

## Skill Version(s):

1.0.0 (source: server release, target metadata, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

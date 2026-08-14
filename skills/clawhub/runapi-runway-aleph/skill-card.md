## Description:

Generate and edit video with Runway Aleph through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and agents use this skill to create, edit, or transform video with Runway Aleph through RunAPI. It guides one-off CLI generation and SDK-based application integration while requiring contract discovery, request validation, and deliverable verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI requests may create paid video generation or editing jobs.

Mitigation: Review request files and authentication state before submitting work, and avoid replacement submissions unless the user authorizes another paid request.

Risk: Video editing may require uploading user-provided source media to RunAPI.

Mitigation: Use only media the user has approved for upload and prefer environment authentication or a known CLI configuration for credentials.

Risk: A successful task status alone may not prove the requested media deliverable is usable.

Mitigation: Download every requested media result and verify each file is non-empty with the expected video MIME type before reporting completion.

## Reference(s):

- [RunAPI Runway Aleph Model Page](https://runapi.ai/models/runway-aleph)
- [RunAPI Runway Aleph Model Documentation](https://runapi.ai/models/runway-aleph.md)
- [Runway Provider Overview](https://runapi.ai/providers/runway.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)
- [Runway Aleph SDK Integration](https://github.com/runapi-ai/runway-aleph-sdk)
- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-runway-aleph)
- [RunAPI Publisher Profile](https://clawhub.ai/user/runapi-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, JSON request files, SDK integration notes, and downloaded media deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires RunAPI authentication for execution and validates generated media files before completion.]

## Skill Version(s):

0.2.9 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

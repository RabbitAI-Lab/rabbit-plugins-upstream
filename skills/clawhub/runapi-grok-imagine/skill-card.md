## Description:

Generate and edit images and videos with Grok Imagine through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to create, edit, animate, and verify Grok Imagine media outputs through RunAPI. Developers can also use it to integrate the current RunAPI SDK and product contract into applications or backend workers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill may upload selected local media to RunAPI or xAI-backed services.

Mitigation: Review generated request files and media inputs before submission, especially when handling sensitive media.

Risk: RunAPI requests may consume paid API credits.

Mitigation: Submit tasks only after authentication, request shape, and expected outputs are confirmed, and avoid replacement paid requests without user authorization.

Risk: Authentication, contract discovery, or output verification failures can make a generated media task incomplete or unsafe to report as finished.

Mitigation: Stop when authentication, contract discovery, or deliverable verification fails, and preserve task or error evidence for review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-grok-imagine)
- [RunAPI Grok Imagine Homepage](https://runapi.ai/models/grok-imagine)
- [Grok Imagine Model Overview, Pricing, and Rate Limits](https://runapi.ai/models/grok-imagine.md)
- [xAI Provider Overview](https://runapi.ai/providers/xai.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)
- [Grok Imagine SDK Integration](https://github.com/runapi-ai/grok-imagine-sdk)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with shell commands, JSON request and response files, SDK code, and downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include RunAPI task JSON, result JSON, generated images, generated videos, and SDK integration guidance.]

## Skill Version(s):

0.2.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

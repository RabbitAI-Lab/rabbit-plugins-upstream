## Description:

ClawVision 1.0.6 improves ClawHub security review transparency by rewriting the description and removing the unused skill_workshop permission.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monaxamo](https://clawhub.ai/user/monaxamo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use ClawVision to turn an explicitly selected chat session into a local visual summary and export package. It creates session-summary artifacts for review, sharing, or presentation after the user confirms scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads a chosen conversation and may summarize sensitive content into local export files.

Mitigation: Use it only on conversations reviewed as safe; avoid chats containing secrets, credentials, personal data, or internal identifiers unless export is explicitly intended.

Risk: Generated summary files can retain sensitive session details after creation.

Mitigation: Review generated files before sharing and keep outputs in an appropriate local workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/monaxamo/skills/clawvision-publish-106)
- [Project homepage](https://github.com/monaxamo/clawvision)

## Skill Output:

**Output Type(s):** [Files, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Self-contained HTML, PNG screenshots, Markdown summary, PowerPoint deck, and output-path text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated locally from a JSON session summary with optional language, preset, output directory, and export-format settings.]

## Skill Version(s):

1.0.6 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

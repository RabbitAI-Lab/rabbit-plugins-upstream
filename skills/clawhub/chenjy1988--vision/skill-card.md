## Description:

Image analysis using Google Gemini vision models for describing images, extracting text from images, analyzing visual content, comparing images, and answering questions about JPG, PNG, GIF, or WebP inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenjy1988](https://clawhub.ai/user/chenjy1988)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when a text-only agent needs to inspect a user-provided image, screenshot, UI capture, error dialog, chart, design mockup, or similar visual input through Google Gemini.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and the user's question are sent to Google Vertex AI using the user's Google project credentials.

Mitigation: Use the skill only when that external processing is acceptable, and avoid sending screenshots, documents, credentials, private records, or other sensitive content unless approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenjy1988/skills/vision)
- [Google Vertex AI Gemini generateContent endpoint](https://aiplatform.googleapis.com/v1/projects/{project})

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Plain text from the vision model, with shell command usage examples in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes one image per invocation; the script configures a maximum response length of 4096 output tokens.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

This skill helps fashion brands, buyers, designers, and social media content teams turn authorized apparel references into multi-scene AI-HIVE lookbook workflows, prompts, runnable commands, and quality checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External fashion brands, buyers, designers, and social media teams use this skill to plan and execute multi-scene lookbook content for the same garment across commerce, advertising, marketing, livestream, and social channels. It produces reviewable plans first, then can guide AI-HIVE image or video generation after the user confirms parameters and potential costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference media are sent to AI-HIVE for generation.

Mitigation: Use only authorized, non-private source media and review inputs before submitting API calls.

Risk: Image or video generation can trigger paid AI-HIVE calls.

Mitigation: Show and confirm the model, routing mode, batch size, parameters, and price snapshot before submitting jobs; start with small batches.

Risk: API keys may be exposed if copied into scripts, logs, screenshots, or committed files.

Mitigation: Use environment variables or the init command for credentials, keep placeholder keys in examples, and avoid logging secrets.

Risk: Generated lookbook content can drift from actual garment details or imply unverified claims.

Mitigation: Keep garment structure, color, logo, and text anchors fixed; mark uncertain facts for review and require human approval before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/fashion-multi-scene-lookbook-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON task records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prompts, production blueprints, reference-image strategy, batch-variant plans, task IDs, status records, and local output paths.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

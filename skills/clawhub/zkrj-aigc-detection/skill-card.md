## Description:

Runs 睿小鉴 AI-generated content and watermark detection for images, text, audio/video, and documents, then reports the conclusion with confidence and evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruixiaojian](https://clawhub.ai/user/ruixiaojian)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to check whether user-provided images, text, audio/video, or documents are AI-generated and to receive a concise detection result with confidence, rationale, and returned evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided content and files are uploaded to the 睿小鉴 backend for detection.

Mitigation: Avoid submitting sensitive files unless the user is comfortable with that service processing them.

Risk: The skill stores bearer and refresh tokens locally in ~/.ruijian-token.json.

Mitigation: Remove ~/.ruijian-token.json or revoke access when the skill is no longer used.

Risk: Detection results can be uncertain or incorrect and are not suitable as sole evidence for legal or safety-critical decisions.

Mitigation: Preserve backend-returned conclusions and disclaimers, and recommend professional human review for high-impact decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruixiaojian/skills/zkrj-aigc-detection)
- [RuijianAI detection service](https://agent.ruijianai.com/?from=extension-clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, guidance]

**Output Format:** [Markdown detection report with confidence, evidence, account status, disclaimer, and service link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detection results must preserve backend-returned conclusions and omit unavailable fields rather than inventing evidence.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

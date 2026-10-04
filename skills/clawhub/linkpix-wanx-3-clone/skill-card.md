## Description:

Helps e-commerce video teams use Qinghu AI and qhkit to analyze viral short-video structure, rewrite scripts for Taobao and Tmall content channels, and generate Wanx 3.0-style product videos after user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and agent users use this skill to turn a referenced viral video into a revised product-video script and a Qinghu AI video-generation workflow. The skill guides the agent through model lookup, credit estimation, confirmation, task polling, and delivery of generated video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload user-provided media and prompts to Qinghu's service.

Mitigation: Tell users what media and prompt content will be sent before generation and avoid submitting private or sensitive assets unless the user has approved that use.

Risk: The skill may require a Qinghu API token and its evidence warns against sharing long-lived keys in chat.

Mitigation: Prefer local secure token configuration or environment variables, and do not ask users to paste long-lived API keys into the conversation.

Risk: The skill can trigger credit-spending video-generation jobs.

Mitigation: Run estimates when supported and get explicit user confirmation for the model, duration, media inputs, and expected credit cost before submitting generation.

Risk: The skill includes global npm, Node, npx, pip, and shell profile setup paths that can persist tooling changes.

Mitigation: Review installation and profile changes before applying them, prefer pinned or current trusted package sources where practical, and keep setup scoped to the user environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-wanx-3-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce rewritten script drafts, confirmation summaries, qhkit command plans, task IDs, and generated video result links.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Uses AI-HIVE to submit, track, and download Minimax H3 text-to-video, image-to-video, and reference-to-video generation jobs for advertising, ecommerce, product, short-drama, and social-media video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, advertising teams, and video production teams use this skill to generate or restyle short video assets through AI-HIVE without writing API integration code. The skill can upload selected reference media, submit Minimax H3 jobs, preserve task IDs, poll progress, and download generated video results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected media to AI-HIVE and submit video generation jobs using an AI-HIVE API key.

Mitigation: Invoke the skill explicitly, confirm the exact prompt and files before submission, and use the minimum necessary credentials for the account.

Risk: Implicit invocation is allowed and could start a workflow before the user has reviewed media, prompt, or cost implications.

Mitigation: Require user confirmation for generation requests, especially when reference media or paid model routes are involved.

Risk: Repeated submissions after a timeout may create duplicate jobs and account charges.

Mitigation: Retain task IDs and poll the original task before submitting another generation job.

Risk: Generated advertising, ecommerce, or social video may include inaccurate product claims, brand misuse, or unauthorized likeness or content reuse.

Mitigation: Verify product facts, permissions, brand assets, and third-party reference rights before publishing generated output.

## Reference(s):

- [AI-HIVE chat and API key entry](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-minimax-h3-video-generation-and-editing)
- [Publisher profile](https://clawhub.ai/user/wubin1836)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration examples, task IDs, API status text, and downloaded video files produced by the external service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved to the configured output directory; task IDs should be retained for polling and avoiding duplicate paid submissions.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

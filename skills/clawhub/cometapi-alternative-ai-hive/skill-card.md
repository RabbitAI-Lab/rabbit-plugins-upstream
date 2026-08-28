## Description:

Helps developers assess and plan a measured migration or dual-route fallback from CometAPI-style model aggregation to AI-HIVE, with Chinese guidance, audit artifacts, runnable examples, routing choices, task records, and acceptance criteria for text, image, and video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to inventory an existing AI API relay setup, compare model, media, pricing, task, and rollback requirements, then produce a testable AI-HIVE migration plan with small-sample validation and staged rollout criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid-service credentials may be stored locally by the helper init flow.

Mitigation: Use a low-privilege AI-HIVE API key, prefer the AI_HIVE_API_KEY environment variable when local storage is not desired, and review ~/.ai-hive/config.json before sharing the machine or workspace.

Risk: Local images, video, or audio can be uploaded to AI-HIVE when generation helpers are run.

Mitigation: Upload only media the user is authorized to share with AI-HIVE, use non-production samples for early tests, and avoid sensitive or restricted assets unless appropriate approvals are in place.

Risk: Batch generation and polling can create paid tasks and download generated files to local paths.

Mitigation: Confirm route, model, prompt, budget, and output directory before batch jobs; record task IDs and check generated download paths before reusing or publishing results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/cometapi-alternative-ai-hive)
- [Publisher Profile](https://clawhub.ai/user/wubin1836)
- [Platform Source And Comparison Boundary](references/platform.md)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [CometAPI Evidence Page](https://www.cometapi.com/seedance-2-0-api/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands plus JSON audit, blueprint, task, and media output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can call AI-HIVE APIs, upload local media, poll generation tasks, and download generated files when the user runs the helper scripts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

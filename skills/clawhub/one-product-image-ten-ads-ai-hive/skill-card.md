## Description:

This skill helps ecommerce and advertising teams turn one authorized product image into ten distinct ad concepts, scripts, first-frame prompts, generation tasks, deduplication notes, and a testing plan using AI-HIVE workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, ecommerce operators, agency teams, and developers use this skill to plan and execute Chinese ad-creative batches from limited product imagery while tracking facts, authorization, routing, cost posture, task status, and review gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires an AI-HIVE API key for generation calls.

Mitigation: Use environment variables or the documented local config path, keep placeholders in examples, and avoid storing or sharing real API keys in prompts, logs, screenshots, or repositories.

Risk: Product images or reference media may be uploaded to AI-HIVE or object storage.

Mitigation: Confirm the user has rights to use the media before upload and restrict unverified references to abstract structure or newly created concepts.

Risk: Image and video generation can incur costs and may duplicate work if submitted repeatedly.

Mitigation: Show final parameters and routing before paid execution, start with a small sample, keep task records, and check inputs or task IDs before expanding a batch.

Risk: Generated ad concepts, deduplication notes, and test plans are workflow outputs rather than guarantees of performance, compliance, or factual accuracy.

Mitigation: Require human review for product claims, pricing, platform rules, legal constraints, and any statements about performance, ranking, sales, or return on investment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/one-product-image-ten-ads-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown workflow sections with inline shell commands; helper scripts can produce JSON briefs, local media outputs, and task records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use AI-HIVE API calls, media uploads, asynchronous polling, price snapshots, and local file outputs after the user supplies credentials and confirms cost-bearing generation.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

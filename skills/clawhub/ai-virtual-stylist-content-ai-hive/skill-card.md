## Description:

Helps apparel brands, buyer shops, fashion creators, and private-domain operators turn real SKU inputs into virtual-stylist themes, lookbook concepts, short-video scripts, prompts, runnable AI-HIVE commands, and review-ready commerce content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External apparel, ecommerce, and content teams use this skill to plan and generate Chinese virtual-stylist marketing deliverables from authorized product facts, SKU images, target audiences, channel constraints, and budget preferences. It is intended for reviewable commercial content workflows where generated assets, product claims, and possible cost-generating AI-HIVE calls remain under human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or reference media and prompts may be sent to AI-HIVE during upload or generation.

Mitigation: Use only authorized, non-sensitive media and do not use the upload command for unrelated sensitive files.

Risk: Image or video generation calls can incur cost.

Mitigation: Confirm prompt, mode, routing preference, model configuration, and price snapshot before submission; start with a small sample for batch work.

Risk: Commerce content can contain inaccurate SKU, price, inventory, authorization, or product-claim statements.

Mitigation: Keep SKU, price, inventory, authorization, and product claims under human review, and mark unverified facts as pending confirmation.

Risk: The AI-HIVE API key is stored or provided locally for API calls.

Mitigation: Use environment variables or the local config flow, keep file permissions restricted, and do not place keys in scripts, logs, screenshots, or release artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-virtual-stylist-content-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with command examples, JSON task records, prompts, scripts, and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE task IDs, pricing snapshots, local file paths, and generated media download records when the user confirms generation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

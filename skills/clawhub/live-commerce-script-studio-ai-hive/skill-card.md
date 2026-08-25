## Description:

This skill helps live-commerce teams turn product facts, audience questions, pricing rules, inventory constraints, and campaign goals into Chinese live-selling scripts, short-video plans, AI-HIVE generation commands, and review checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, live-commerce operators, brand merchants, and field-control teams use this skill to plan Chinese live-selling sessions and derivative short-video assets from authorized product facts, media, prices, inventory rules, and platform constraints. It produces reviewable scripts, prompts, task plans, runnable commands, and acceptance criteria before any billable AI-HIVE generation task is submitted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE API credentials may be supplied by the user and may be stored locally by helper scripts.

Mitigation: Use environment variables or the local config path intentionally, avoid pasting real keys into prompts or shared files, and inspect generated files and logs before distribution.

Risk: Image or video generation commands may upload media and create billable tasks.

Mitigation: Confirm media authorization, prompt text, routing mode, model choice, and budget before execution; run a small sample before batch generation.

Risk: Live-commerce copy can misstate product facts, performance claims, prices, inventory, endorsements, or platform compliance.

Mitigation: Require source-backed product facts and manual review before publication, and avoid unsupported guarantees about traffic, sales, ranking, approval, or return on investment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/live-commerce-script-studio-ai-hive)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with scripts, prompts, checklists, JSON task records, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE routing, model, price snapshot, taskId, status, and file-location details when generation tasks are used.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

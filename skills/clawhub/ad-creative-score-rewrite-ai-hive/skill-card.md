## Description:

Helps ad buyers, creative teams, and merchants turn Chinese ad-creative review requests into heuristic scores, evidence-backed rewrite priorities, scripts, prompts, runnable AI-HIVE commands, and quality checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, creative teams, ad buyers, and merchants use this skill to score and rewrite Chinese e-commerce, social, short-drama, and paid-ad creatives before publication. It can also prepare scripts, prompts, task records, and runnable AI-HIVE commands for user-confirmed image or video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected reference images, videos, or audio may be uploaded to AI-HIVE during generation or upload commands.

Mitigation: Use only media the user is authorized to upload, avoid sensitive assets, and confirm upload intent before running API-backed commands.

Risk: The init flow can store an AI-HIVE API key locally.

Mitigation: Use environment variables when possible, protect local config files, and avoid exposing API keys in logs, screenshots, or version control.

Risk: Generation tasks may trigger paid external API calls.

Mitigation: Confirm the prompt, model, routing mode, parameters, and price snapshot before submitting generation tasks; run a small sample before batch work.

Risk: Creative scores are heuristic and are not real campaign performance predictions.

Mitigation: Treat scores as prioritization guidance and validate claims, platform fit, and performance with real product, platform, and campaign data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ad-creative-score-rewrite-ai-hive)
- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown with inline shell commands, generated JSON files, and optional downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include heuristic scoring reports, rewrite plans, scripts, prompts, model routing choices, price snapshots, task IDs, task status, and local file paths.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

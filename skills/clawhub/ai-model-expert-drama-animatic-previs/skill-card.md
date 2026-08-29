## Description:

Helps short-drama, comic-drama, brand, ecommerce, and distribution teams turn ideas, scripts, character images, or reference media into production briefs, storyboards, animatic/previs plans, generation prompts, and AI-HIVE image or video generation commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, studios, brands, ecommerce teams, and developers use this skill to plan short-drama or comic-drama projects, lock characters and scenes, generate shot-level prompts, submit AI-HIVE media generation tasks, and track or download results. It is suited to commercial pre-production workflows where users provide authorized source materials and review generated outputs before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires an AI-HIVE API key and may upload user-selected media files to AI-HIVE.

Mitigation: Use environment-variable credentials or the disclosed local config file, keep the key private, and upload only media that is approved for the generation task.

Risk: Generated or reference-based short-drama media can raise copyright, likeness, brand-fact, age-safety, or platform-compliance issues.

Mitigation: Use authorized source materials, avoid copying protected expression, confirm facts and product claims with the user, and review generated outputs before commercial delivery.

Risk: Repeated submissions or task retries may create unnecessary cost if a generation task is still running.

Mitigation: Record task IDs, query existing tasks after timeouts, and review model, quantity, routing, and pricing snapshots before submitting batch jobs.

## Reference(s):

- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-animatic-previs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, media files]

**Output Format:** [Markdown guidance with inline shell commands, JSON blueprint files, configuration instructions, task identifiers, and generated image or video files from AI-HIVE.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI-HIVE API key for API-backed generation; supports environment-variable or local config credentials, media upload, task polling, optional no-download submission, and cost/speed/success routing.]

## Skill Version(s):

1.0.0 (source: evidence release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

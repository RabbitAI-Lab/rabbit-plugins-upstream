## Description: <br>
Resilient ImageGen stabilizes multi-image generation by turning prompts into a retryable serial job queue, selecting an available generation route, and producing a reviewable manifest for downstream image workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangchao228](https://clawhub.ai/user/yangchao228) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content workflow authors use this skill to manage multi-image generation batches that need retries, resumability, saved output paths, and human review gates. It is most useful when built-in ImageGen is unreliable or when work may need to route through Computer Use, manual ChatGPT handoff, local rendering, or a separately confirmed CLI/API fallback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may coordinate external uploads, paid API use, or state-changing image generation actions. <br>
Mitigation: Require explicit user confirmation before Computer Use submissions, reference uploads, CLI/API fallback, paid calls, or Markdown URL rewrites. <br>
Risk: Generated images can contain incorrect text, invented UI, wrong numbers, logos, watermarks, or other unsuitable content. <br>
Mitigation: Open and inspect every generated image before marking it ready, and use deterministic rendering or downstream correction when exact text or factual diagrams matter. <br>
Risk: Interrupted or partially failed batches can be mistaken for complete output. <br>
Mitigation: Persist a manifest with per-job status, attempts, errors, output paths, and review state, then resume only queued or failed jobs after verifying existing files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yangchao228/skills/resilient-imagegen) <br>
- [Metadata homepage](https://github.com/yangchao228/my_open_skills/tree/main/skills/content/resilient-imagegen) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown run report with queue and failure tables, plus YAML manifest guidance and optional handoff details.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Records selected backend, capability state, retry attempts, output paths, visual QA status, and confirmation gates without storing secrets.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

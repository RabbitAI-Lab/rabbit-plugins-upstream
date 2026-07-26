## Description: <br>
Routes multi-image content jobs through available generation backends, prepares resumable prompt packs with readable-text boundaries, imports outputs under stable filenames, and resumes visual QA. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangchao228](https://clawhub.ai/user/yangchao228) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content-production agents use this skill to recover image-generation workflows when the built-in generator is unavailable or unreliable. It prepares prompt packs, routes to approved generation backends, imports results, and supports visual QA with strict readable-text controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local handoff folders may contain local paths, reference images, generated files, and working reports. <br>
Mitigation: Keep the handoff directory out of public commits and review files before sharing or publishing. <br>
Risk: Computer Use can transmit prompts or reference images to an authenticated ChatGPT session. <br>
Mitigation: Use only approved materials and require action-time confirmation before the first prompt or file upload. <br>
Risk: Generated images may include invented or unapproved readable text, identifiers, filenames, or metrics. <br>
Mitigation: Apply strict readable-text allowlists, import results through local QA, and use deterministic or mixed overlays when exact text is required. <br>


## Reference(s): <br>
- [UI recovery rules](artifact/references/ui-recovery.md) <br>
- [Optional ChatGPT ZIP batches](artifact/references/zip-batch.md) <br>
- [ClawHub metadata homepage](https://github.com/yangchao228/my_open_skills/tree/main/skills/content/chatgpt-image-handoff) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with JSON state files, prompt files, shell commands, and image handoff artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local handoff folders, stable imported filenames, checksums, QA reports, contact sheets, and optional mixed-overlay reports.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

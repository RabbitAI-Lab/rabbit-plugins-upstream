## Description:

This skill helps apparel brands, photography teams, cross-border sellers, and product designers turn authorized clothing references into AI-HIVE model-swap image workflows, prompts, runnable commands, and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External apparel teams and content operators use this skill to plan and run AI-HIVE apparel model-swap image production while preserving garment structure, texture, color, logo accuracy, and platform-specific deliverables. Developers and agents can also use its scripts to create a production brief, upload authorized media, query model and pricing data, submit generation tasks, poll task status, and download results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference media and prompts selected by the user are sent to AI-HIVE.

Mitigation: Use only authorized media and review prompt content before upload or generation.

Risk: Generation commands can incur API charges after confirmation.

Mitigation: Confirm final parameters, routing mode, model choice, and batch size before submitting tasks; start with a small batch.

Risk: API keys may be exposed through logs, screenshots, files, or repositories.

Mitigation: Use environment variables or the local config file, keep placeholders in examples, and avoid recording real keys in outputs.

Risk: Generated apparel images may misrepresent garment structure, colors, logos, endorsements, or factual claims.

Mitigation: Perform human review against product facts and authorized assets before publishing generated marketing visuals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/apparel-model-swap-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with runnable shell commands, JSON task records, and generated local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create blueprint JSON files and download generated media after confirmed AI-HIVE API task execution.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

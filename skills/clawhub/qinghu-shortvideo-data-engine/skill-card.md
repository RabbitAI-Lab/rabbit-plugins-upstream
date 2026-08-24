## Description:

This skill helps an agent collect Douyin, Xiaohongshu, and Bilibili short-video metrics such as views, likes, shares, saves, and comments, then export the results as an Excel file through QinghuAI qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Social media operators, marketers, and agents use this skill to batch-check owned or competitor short-video performance and retrieve a spreadsheet of platform metrics. It is intended for one-time data collection jobs for supported Douyin, Xiaohongshu, and Bilibili video long links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can spend Qinghu credits through a paid external service.

Mitigation: Run qhkit estimate first, show the estimated credits to the user, and start generate only after explicit approval.

Risk: The skill can prompt installation or upgrade of qhkit, Node, or npm packages.

Mitigation: Prefer a preinstalled trusted qhkit runtime and avoid automatic global installs, Node bootstrapping, or latest-version upgrades unless the environment owner accepts those changes.

Risk: The Qinghu API key is sensitive.

Mitigation: Store the token only in approved configuration or environment variables and avoid exposing it in prompts, command output, logs, or generated artifacts.

Risk: Supported video links are sent to QinghuAI/qhkit for processing.

Mitigation: Use the skill only for links the user intends to process with QinghuAI/qhkit and confirm that source material is appropriate for the intended use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shortvideo-data-engine)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent through qhkit options, estimate, generate, and status commands; completed jobs return downloadable XLSX file links.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

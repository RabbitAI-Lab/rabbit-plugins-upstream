## Description:

This skill helps AIGC, ecommerce, advertising, and developer teams evaluate and plan a cautious migration or dual-route fallback from fal.ai-style generative media APIs to AI-HIVE, producing migration audits, capability mappings, routing plans, runnable examples, task ledgers, and acceptance criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to audit current generative media API usage, compare fal.ai-style workflows with AI-HIVE, and prepare a testable migration plan with sample generation commands, price-snapshot discipline, task tracking, gray rollout, and rollback criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper scripts can use an AI-HIVE API key and create billable generation tasks.

Mitigation: Use a scoped or test API key, set a budget before running generation commands, start with non-production samples, and keep task IDs and price snapshots for review.

Risk: Media generation helpers can upload user-selected images, videos, or audio to AI-HIVE.

Mitigation: Upload only material the user is authorized to process and avoid confidential or regulated media unless the applicable service terms and internal approvals allow it.

Risk: The init flow can persist credentials in a local AI-HIVE configuration file.

Mitigation: Prefer passing credentials through the AI_HIVE_API_KEY environment variable or CLI arguments, and use local credential storage only when its file-permission and workstation risks are acceptable.

Risk: Broad implicit invocation can surface AI-HIVE-specific migration advice in related API-platform discussions.

Mitigation: Confirm the user wants AI-HIVE-specific migration guidance before running scripts, changing configuration, uploading media, or submitting generation tasks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/fal-ai-alternative-ai-hive)
- [Platform Source and Comparison Boundary](references/platform.md)
- [fal.ai Evidence Page](https://fal.ai/seedance-2.0)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON file outputs from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit billable AI-HIVE generation tasks, upload chosen media, poll task status, and download generated media when users run the helper scripts.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

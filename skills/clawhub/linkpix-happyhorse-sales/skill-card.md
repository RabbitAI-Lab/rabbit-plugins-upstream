## Description:

This skill helps ecommerce, brand, livestream commerce, and content teams use qhkit to generate HappyHorse 1.1 product marketing videos from text prompts and optional image, video, or audio references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand merchandise teams, livestream commerce teams, and commercial content creators use this skill to plan, price, submit, monitor, and deliver product advertising videos through qhkit. It is intended for product demos, short-form commerce videos, social ads, and marketplace marketing content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask users to share an API key in chat.

Mitigation: Avoid sending API keys in chat; configure credentials through a protected local secret mechanism or environment variable where possible.

Risk: The skill directs agents to install or upgrade unpinned executable packages.

Mitigation: Prefer a pinned, isolated qhkit installation and review the package source before execution.

Risk: Video generation uploads user-selected files and can spend account credits.

Mitigation: Confirm exactly which files will be uploaded and what credits will be spent before generation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-happyhorse-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit setup steps, model-selection guidance, task IDs, status summaries, generated media URLs, and credit estimates.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

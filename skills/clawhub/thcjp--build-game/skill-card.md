## Description:

构建游戏 helps agents generate and iteratively refine 3D browser game projects from natural-language requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to ask an agent to create or modify 3D browser games, including characters, environments, inventory systems, and other gameplay features. Reviewers should account for the security evidence before using it in production workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence marks the release as suspicious because it is labeled as a 3D game builder while also containing scraping, anti-crawler-bypass, and browser data extraction language.

Mitigation: Review carefully before installing and use only if the publisher narrows the scope to game development or clearly documents consent, limits, and non-bypass requirements.

Risk: The artifact requests broad read, execute, and write authority for agent operation.

Mitigation: Run it in a constrained workspace, review proposed file and shell actions before execution, and avoid exposing secrets or unrelated browser data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/build-game)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with code blocks and optional JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce browser game source changes, development commands, configuration notes, and structured status output.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

HeartFlow is a rule-based discriminator and MCP service that checks AI inputs, drafts, and outputs for trust, safety, manipulation, contradiction, and completion issues without an LLM dependency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yun520-1](https://clawhub.ai/user/yun520-1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use HeartFlow to add a deterministic guardrail around LLM or agent output. It returns gate decisions and findings that help block, rewrite, verify, or pass text and decisions before they reach users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs as a stateful local MCP service with local memory and log files.

Mitigation: Run it in a contained project and review persistence settings before use.

Risk: The security guidance identifies plaintext .env token handling and a localhost authenticated server.

Mitigation: Set an explicit token, restrict access to localhost, and avoid sharing project environments that contain credentials.

Risk: The security summary flags a broad MCP tool surface.

Mitigation: Enable only the tools and routes needed for the deployment and review path-guard settings before connecting clients.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yun520-1/skills/mark-heartflow-skill)
- [ClawHub publisher profile](https://clawhub.ai/user/yun520-1)
- [npm package](https://www.npmjs.com/package/@yun520-1/heartflow)
- [Project repository link from artifact README](https://github.com/yun520-1/mark-heartflow-skill)
- [Project issues link from artifact README](https://github.com/yun520-1/mark-heartflow-skill/issues)
- [Project releases link from artifact README](https://github.com/yun520-1/mark-heartflow-skill/releases)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell commands; runtime usage can return structured JavaScript or MCP result objects.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Gate actions include block, rewrite, verify, and pass, with supporting findings and audit details.]

## Skill Version(s):

6.6.1 (source: server release metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

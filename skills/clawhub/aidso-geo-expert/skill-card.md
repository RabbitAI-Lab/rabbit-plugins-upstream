## Description:

End-to-end GEO workflows for question mining, AI answer monitoring, result retrieval, GEO reporting, and content creation with AIDSO.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tangyuanmile-coder](https://clawhub.ai/user/tangyuanmile-coder)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run AIDSO GEO workflows for question mining, paid AI answer monitoring, result retrieval, GEO reporting, and GEO content creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled runtime uses private encrypted rules and scripts that can execute Node/Python code.

Mitigation: Install only from a trusted publisher, review the release before installation, and run it in a constrained workspace.

Risk: Paid AIDSO monitoring submissions can consume account credits.

Mitigation: Require explicit user confirmation before submission and verify the credit details shown by the skill.

Risk: The workflow connects to AIDSO with an account token and may store local task or report files.

Mitigation: Use a scoped AIDSO token, keep tokens out of chat and logs, and restrict the workspace used for generated files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tangyuanmile-coder/skills/aidso-geo-expert)
- [Publisher profile](https://clawhub.ai/user/tangyuanmile-coder)
- [AIDSO MCP endpoint](https://api.aidso.com/geo_api/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and generated GEO workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local AIDSO task, report, or content files when the selected workflow requires them.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

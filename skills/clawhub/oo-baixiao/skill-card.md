## Description:

Baixiao AI (know-pa.cn). Use this skill for ANY Baixiao AI request -- reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Baixiao AI through an OOMOL-connected account for academic search, citation workflows, knowledge-base search, policy discovery, grant discovery, reviewer suggestions, journal-fit recommendations, and PDF link retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup documents direct remote installer execution for the oo CLI.

Mitigation: Review the installer before running it, or install the oo CLI through a verified package or inspected download.

Risk: Write actions, dynamic call_tool use, personal knowledge-base search, and PDF retrieval may expose account data, alter Baixiao state, or consume credits.

Mitigation: Confirm the exact payload and expected effect before write or destructive behavior, and confirm credit-consuming PDF retrieval before execution.

## Reference(s):

- [Baixiao AI homepage](https://www.know-pa.cn/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-baixiao)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger Baixiao connector actions through the oo CLI; some actions can change state, consume credits, or return account-scoped data.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

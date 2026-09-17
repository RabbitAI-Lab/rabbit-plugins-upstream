## Description:

Enables agents to read Clari Copilot calls, scorecards, topics, and workspace users through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees with connected Clari Copilot access can use this skill through an agent to retrieve call details, transcripts, summaries, scorecards, topics, and workspace users for account review and follow-up workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the oo CLI.

Mitigation: Prefer an independently verified oo CLI installation method and inspect installer contents before execution.

Risk: The skill can read Clari Copilot workspace data from the connected account.

Mitigation: Connect only the intended Clari Copilot account and confirm requested reads match the user's authorization and purpose.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clari-copilot)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Clari Copilot product page](https://www.clari.com/products/copilot/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads Clari Copilot data through oo CLI connector actions; no write or destructive actions are documented in the artifact.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

More Trees helps agents retrieve More Trees account, forest, project, and species information and plant or gift trees through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents used by More Trees customers or operators can retrieve connected account details, forest statistics, planting projects, and available tree species. They can also prepare planting or gifting requests, with explicit user confirmation before any action that consumes credits or affects recipients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can plant or gift trees, which may consume planting credits or affect recipients.

Mitigation: Before running a planting or gifting action, require the agent to show the exact final payload, recipient details, test-mode status, expected credit impact, and obtain explicit approval immediately before execution.

Risk: The setup guidance includes remote installer commands for the oo CLI.

Mitigation: Install only after reviewing the setup steps and confirming the oo CLI source is trusted and verified.

Risk: Incorrect payloads may act on the user's connected More Trees account.

Mitigation: Fetch the live connector schema before building payloads and keep all write actions gated behind user confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-more-trees)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [More Trees homepage](https://www.moretrees.eco)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or connector results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call live More Trees connector actions through the oo CLI; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

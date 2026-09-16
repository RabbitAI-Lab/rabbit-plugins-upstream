## Description:

Autoblogging.ai (autoblogging.ai). Use this skill for Autoblogging.ai requests involving reading, creating, and updating data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Autoblogging.ai through an OOMOL-connected account, inspect live action schemas, create article-generation jobs, and fetch article job status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installer commands for the oo CLI.

Mitigation: Do not let an agent run the first-time installer automatically; use a pinned, verified oo CLI installation path before enabling the skill.

Risk: Autoblogging.ai actions are mediated through OOMOL, which injects credentials server-side.

Mitigation: Install only when use of OOMOL as an intermediary is acceptable for the account and workflow.

Risk: The create_article action can spend credits or create service-side state.

Mitigation: Confirm the exact create_article payload and intended effect with the user before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-autoblogger)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Autoblogging.ai homepage](https://autoblogging.ai)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and requires confirmation before write or destructive operations.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

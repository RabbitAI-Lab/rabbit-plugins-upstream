## Description:

Gong (gong.io). Use this skill for ANY Gong request - searching and reading data. Whenever a task involves Gong, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to search and read Gong calls, call transcripts, users, and call outcome configuration through an OOMOL-connected Gong account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unverified internet installer commands that can execute code on the user's computer.

Mitigation: Do not let an agent run curl|bash or irm|iex automatically; prefer a verified, pinned installer or official package flow.

Risk: The skill can read Gong call, transcript, and user data available to the connected account.

Mitigation: Install and use it only with an account whose Gong access is appropriate for the task, and review returned data before sharing it further.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gong)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Gong homepage](https://www.gong.io/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Gong call, transcript, user, and action metadata available to the connected account.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

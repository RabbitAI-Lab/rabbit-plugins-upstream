## Description:

OpenPageRank (openpagerank.com). Use this skill for ANY OpenPageRank request: searching and reading data through the OOMOL-connected OpenPageRank connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to look up OpenPageRank scores for one or more domains and receive normalized rank metadata through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified internet installer commands, and the security verdict is suspicious.

Mitigation: Use verified OOMOL installation documentation or pinned, checked artifacts; do not allow an agent to run inline curl-to-bash or Invoke-Expression installer commands automatically.

Risk: Routine use sends requested domain lookups through OOMOL/OpenPageRank.

Mitigation: Use the skill only when that data sharing is acceptable and rely on the documented server-side credential handling instead of exposing raw tokens to the agent.

## Reference(s):

- [OpenPageRank homepage](https://openpagerank.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-openpagerank)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include normalized PageRank metadata returned by the OpenPageRank connector.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

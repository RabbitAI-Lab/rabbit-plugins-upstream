## Description:

tl;dv (tldv.io). Use this skill for ANY tl;dv request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to read tl;dv meeting records, notes, and transcripts through an OOMOL-connected account, and to import publicly accessible recording URLs when the user confirms the write action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes installing the oo CLI with a remote script.

Mitigation: Review the installation step before use and prefer verified official instructions with a pinned version or checksum/signature verification where available.

Risk: Enabled read actions can access private tl;dv meeting notes and transcripts.

Mitigation: Use the skill only with the intended connected account and review requested meeting identifiers or filters before running actions.

Risk: The import action changes tl;dv state by submitting a recording URL.

Mitigation: Confirm the exact recording URL and expected effect with the user before running the write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tldv)
- [tl;dv homepage](https://tldv.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON data from tl;dv connector actions when the agent runs the oo CLI.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

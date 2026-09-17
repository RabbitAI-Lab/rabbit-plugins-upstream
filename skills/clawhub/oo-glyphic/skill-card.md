## Description:

Glyphic lets an agent search and read Glyphic calls, transcripts, summaries, media metadata, snippets, insights, playbooks, and tags through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent retrieve Glyphic call records, transcripts, summaries, snippets, media metadata, playbooks, playbook versions, and organization call tags. It is useful when conversational or sales-call information needs to be inspected through an existing OOMOL-connected Glyphic account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can install the oo CLI through remote shell commands.

Mitigation: Review setup commands before use and prefer a pinned, verifiable oo CLI release or official package-manager installation path.

Risk: Connecting Glyphic can allow access to organization call, transcript, media, and playbook data through the user's OOMOL-connected account.

Mitigation: Connect Glyphic only when that data access is appropriate for the intended workspace and account permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-glyphic)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Glyphic homepage](https://www.goairspeed.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Glyphic call, transcript, media, snippet, insight, playbook, and tag data returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

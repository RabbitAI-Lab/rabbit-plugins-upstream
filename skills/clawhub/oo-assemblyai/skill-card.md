## Description:

Operate AssemblyAI through an OOMOL-connected account to create, delete, list, and retrieve transcript data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate AssemblyAI through an OOMOL-connected account, including creating transcripts, listing transcripts, retrieving transcript details, and getting paragraph or sentence views of transcripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags unverified remote installer commands as high impact.

Mitigation: Use an official package or verified download path instead of running curl|bash or irm|iex installer commands blindly.

Risk: The skill can create and delete AssemblyAI transcripts through a connected account.

Mitigation: Review write and delete requests carefully, confirm the exact payload and target transcript, and require explicit approval for destructive actions.

Risk: OOMOL brokers access to the user's AssemblyAI account.

Mitigation: Install only when the user is comfortable with OOMOL-brokered access and has connected the intended AssemblyAI account.

## Reference(s):

- [ClawHub AssemblyAI Skill](https://clawhub.ai/oomol/skills/oo-assemblyai)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [AssemblyAI Homepage](https://www.assemblyai.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke AssemblyAI connector actions through the oo CLI and return JSON responses containing action data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

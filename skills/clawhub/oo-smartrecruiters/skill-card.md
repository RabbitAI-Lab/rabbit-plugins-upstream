## Description:

Use this skill for SmartRecruiters search and read workflows through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and recruiting operations users use this skill to inspect SmartRecruiters action schemas, read candidate and job details, and search jobs or candidates from an OOMOL-connected SmartRecruiters account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags setup instructions that execute remote installer scripts through shell commands.

Mitigation: Install the oo CLI through a trusted, verifiable method and do not allow an agent to run curl-to-bash or irm-to-iex installer commands automatically.

Risk: The skill operates through a connected SmartRecruiters account and may expose recruiting data through read and search actions.

Mitigation: Connect only the intended SmartRecruiters account and scopes, and review returned candidate or job data before sharing it outside the authorized workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-smartrecruiters)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [SmartRecruiters Homepage](https://www.smartrecruiters.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

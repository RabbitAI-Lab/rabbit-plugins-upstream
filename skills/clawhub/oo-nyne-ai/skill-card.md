## Description:

Nyne.ai (nyne.ai). Use this skill for ANY Nyne.ai request -- reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Nyne.ai through an OOMOL-connected account, including searches, enrichment requests, polling request status, and checking usage balances.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include remote shell installer commands.

Mitigation: Install the oo CLI only from verified official releases or a trusted package manager with integrity checks, and do not allow an agent to run curl|bash or irm|iex automatically.

Risk: Nyne.ai submit actions can create search or enrichment requests.

Mitigation: Confirm the exact payload and intended effect before running write-tagged submit actions.

## Reference(s):

- [Nyne.ai homepage](https://nyne.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nyne-ai)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector responses that include data and meta.executionId when actions run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

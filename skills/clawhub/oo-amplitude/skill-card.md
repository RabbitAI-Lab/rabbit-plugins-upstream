## Description:

Use this skill to search and read Amplitude data through the OOMOL-connected Amplitude connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Amplitude event metrics, user activity summaries, visible event lists, and user search results through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can lead users to execute remote installer scripts directly in a shell.

Mitigation: Install the oo CLI only through a verified, pinned, or package-manager method before running Amplitude actions.

Risk: The skill operates through an OOMOL-connected Amplitude account and may expose account-scoped analytics data.

Mitigation: Run only Amplitude actions the user understands, and rely on live schema inspection before submitting requests.

## Reference(s):

- [Amplitude homepage](https://amplitude.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-amplitude)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON data]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs read-oriented Amplitude connector actions through the oo CLI after inspecting live schemas.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

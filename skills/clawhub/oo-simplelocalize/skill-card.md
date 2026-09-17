## Description:

SimpleLocalize helps agents read, create, update, and delete SimpleLocalize data through the OOMOL oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and localization operators use this skill to inspect SimpleLocalize projects, list languages and translations, and create or update localization data through an OOMOL-connected account. It also supports destructive language deletion when the user has explicitly confirmed the target and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports install commands that execute unverified code downloaded from the internet.

Mitigation: Use this skill only if the OOMOL SimpleLocalize connector is trusted, install the oo CLI through a verified reviewed method, and do not let an agent run pasted curl|bash or irm|iex commands automatically.

Risk: Create and update actions can change SimpleLocalize project state.

Mitigation: Fetch the live action schema, review the exact payload and intended effect, and require explicit approval before running write actions.

Risk: The delete_language action is destructive and can remove SimpleLocalize language data.

Mitigation: Confirm the target language and effect with the user, then require explicit approval before running the destructive action.

## Reference(s):

- [SimpleLocalize homepage](https://simplelocalize.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub SimpleLocalize skill page](https://clawhub.ai/oomol/skills/oo-simplelocalize)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include SimpleLocalize connector responses with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

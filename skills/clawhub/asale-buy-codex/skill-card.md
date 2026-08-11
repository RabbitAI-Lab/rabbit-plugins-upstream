## Description:

Switch Codex between buying from the asale market and using its own subscription, and show which running sessions are still using the previous configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Codex users use this skill to route future Codex sessions through the local asale buying flow, select market models, restore personal-subscription behavior, and identify running sessions that still use old configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install method runs a remote script directly on the user's computer.

Mitigation: Review the installer source before running it and prefer a signed or checksummed release when available.

Risk: Enabling the skill lets the local asale daemon persistently modify Codex configuration and authentication files to route future Codex requests through asale.

Mitigation: Confirm the intended switch state and model selection before enabling, then verify the Codex configuration after the change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/asale-buy-codex)
- [asale homepage](https://asale.ai)
- [asale source repository](https://github.com/asale-ai/asale)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers local daemon status, authentication errors, model selection, configuration switching, and process-reporting caveats.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 0.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

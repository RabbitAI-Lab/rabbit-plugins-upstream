## Description:

Switches Gemini CLI between buying requests from the asale market and using the user's own subscription, while identifying running Gemini CLI sessions that still use older configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route Gemini CLI through the local asale daemon when they want future Gemini CLI starts to buy from the asale market instead of consuming their own Gemini subscription. It also helps them check which already-running Gemini CLI sessions are still using older configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer asks the user to run a remote script with full user privileges.

Mitigation: Install only when the asale publisher and hosting path are trusted, and review the installer source or use an approved internal installation process before deployment.

Risk: The skill reads a local daemon token and changes Gemini CLI configuration so future starts can route requests and spending through asale's market.

Mitigation: Verify the switch state in the asale UI, keep the daemon token local, and turn the switch off when market routing is no longer desired.

Risk: Already-running Gemini CLI sessions may keep their old startup configuration.

Mitigation: Use the process listing only to inform the user which sessions may need manual restart; do not signal or kill those processes.

## Reference(s):

- [asale homepage](https://asale.ai)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/asale-buy-gemini-cli)
- [ClawHub publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill provides local daemon RPC examples, configuration state guidance, and safety-sensitive reminders about daemon authentication and running sessions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

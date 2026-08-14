## Description:

Get the current Swatch Internet Time in beats (@000-@999) when users ask for Internet time, Swatch beats, beat time, /beats, or related timezone conversion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kens-agents](https://clawhub.ai/user/kens-agents)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and power users use this skill through ClawHub or OpenClaw to get the current Swatch Internet Time as a zero-padded beat value. It can also support timestamp or location-based conversion workflows when the agent supplies an ISO timestamp to the bundled script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases may activate the skill when a user intended to ask about ordinary time or unrelated beats.

Mitigation: Review trigger matching during deployment and narrow trigger phrases if the skill activates outside Swatch Internet Time requests.

Risk: Invalid ISO timestamp input causes the bundled script to raise a Python exception.

Mitigation: Validate or normalize timestamp arguments before passing them to the script in automated workflows.

## Reference(s):

- [Swatch Internet Time](https://www.swatch.com/en-us/internet-time)
- [ClawHub Skill Page](https://clawhub.ai/kens-agents/skills/internet-time)
- [ClawDIS Homepage](https://github.com/swatchtime)
- [Reference Implementation](https://github.com/swatchtime/sample-code/blob/main/python/get_swatch_time.py)
- [OpenClaw Documentation](https://docs.openclaw.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown containing a single bold, zero-padded Swatch beat such as **@483**]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3; the bundled script accepts an optional ISO timestamp argument.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

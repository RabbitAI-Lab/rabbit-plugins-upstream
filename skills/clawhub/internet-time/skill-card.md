## Description:

Get the current Swatch Internet Time in beats (@000-@999).

This skill is ready for commercial/non-commercial use.

## Publisher:

[kens-agents](https://clawhub.ai/user/kens-agents)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer requests for Swatch Internet Time, current beat time, or beat-time conversion with a concise beat value.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad time-related trigger phrases may cause the agent to answer with a Swatch beat time in ordinary time conversations.

Mitigation: Use the skill when the user specifically asks for Internet Time, Swatch beats, /beats, or beat-time conversion; otherwise answer normally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kens-agents/skills/internet-time)
- [Project homepage](https://github.com/swatchtime)
- [Swatch Internet Time specification](https://www.swatch.com/en-us/internet-time)
- [Swatch Time Python reference implementation](https://github.com/swatchtime/sample-code/blob/main/python/get_swatch_time.py)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [A single Swatch beat time string such as **@483**, with optional shell-command guidance for manual script execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Beat values are zero-padded to three digits in the @000-@999 range.]

## Skill Version(s):

1.0.6 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

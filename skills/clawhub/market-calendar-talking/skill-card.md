## Description:

Turns a user-supplied public trading calendar and authorized stills into short narrated calendar clips, one clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Wealth advisors and educators use this skill to turn already-public session, holiday, and settlement dates into short talking clips using stills and voices they are authorized to use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Beatra device token grants broad access to paid media generation.

Mitigation: Use only an account whose generation permissions and possible credit spend are acceptable; approve each paid stage and check its live cost.

Risk: Package files update silently by default.

Mitigation: Review updates before installing, or disable automatic updates with `python3 scripts/mcp_client.py update --auto off`.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/market-calendar-talking)
- [Beatra skill homepage](https://beatra.ai/skills/market-calendar-talking)
- [Calendar talking workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Video links, Audio links]

**Output Format:** [Markdown slot list and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One short talking clip per authorized still; no stitching.]

## Skill Version(s):

0.1.8 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

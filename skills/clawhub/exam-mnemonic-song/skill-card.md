## Description:

Turns an exam knowledge point and supplied facts into a replayable mnemonic song, with an option to build a set for the remaining syllabus.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Exam candidates, teachers, and coaches use this skill to turn supplied study facts into a labeled lyric sheet and, after approval, a generated mnemonic song for each knowledge point.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization grants a shared Beatra device token with broader media and tool access than mnemonic songs require.

Mitigation: Connect only if comfortable with the full account access; keep the token private and review device revocation options.

Risk: Silent package updates are enabled by default and may change code without a separate approval.

Mitigation: Consider disabling automatic updates with `python3 scripts/mcp_client.py update --auto off` and reviewing changes before manual updates.

Risk: Music generation consumes credits, and a retry after an uncertain response may duplicate a charge.

Mitigation: Confirm the live price and obtain approval before each set; recover the existing task using the same request identity rather than creating a new one.

Risk: Uninstalling the last Beatra skill may affect the shared device connection.

Mitigation: Check which other Beatra skills use the connection and review account and device revocation before uninstalling.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/exam-mnemonic-song)
- [Exam mnemonic workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Audio links]

**Output Format:** [Labeled lyric sheet and song result with playback link when generation succeeds]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated songs are billable; reports actual duration and charged credits when available.]

## Skill Version(s):

0.1.8 (source: server-resolved release and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

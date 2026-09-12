## Description:

Creates exam mnemonic lyric sheets from user-provided knowledge points and, after explicit approval, generates one Beatra text-to-music song per knowledge point.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Training schools, exam coaches, teachers, and candidates use this skill to turn supplied exam facts into a reviewed mnemonic lyric sheet and generated study song, one knowledge point at a time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra account permissions beyond mnemonic music generation.

Mitigation: Review the requested access before authorization and install only if the user accepts those broader media and account permissions.

Risk: The skill stores a reusable local Beatra credential.

Mitigation: Keep the credential local and private, and use the bundled uninstall or disconnect flow when access should be revoked.

Risk: The bundled client can silently update package files.

Mitigation: Disable automatic updates for the installation when deterministic package contents are required.

Risk: Generated music calls can spend Beatra credits.

Mitigation: Require explicit approval before each paid generation call, read current pricing, and report actual charged credits after task completion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/exam-mnemonic-song)
- [Beatra skill homepage](https://beatra.ai/skills/exam-mnemonic-song)
- [Exam mnemonic workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown with lyric sheets, approval cards, inline shell commands, and generated media artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses one approved paid generation call per knowledge point; reports actual duration and charged credits when available.]

## Skill Version(s):

0.1.2 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

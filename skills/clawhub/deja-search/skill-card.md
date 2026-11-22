## Description:

Searches a user's past AI coding sessions with the deja CLI to retrieve prior decisions, preferences, and work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vshulcz](https://clawhub.ai/user/vshulcz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can search their own past AI coding sessions for decisions, preferences, and prior fixes before planning, editing, reviewing, or recommending changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill searches broadly across coding histories, and its fallback may download and run an unpinned package; it also guides persistent cross-agent rule changes.

Mitigation: Review the history-search scope, inspect and pin the package before installation, require approval before package execution, and review rule changes before applying them.

Risk: The security scan is incomplete because two referenced local paths were missing.

Mitigation: Review the missing paths and rerun the security scan before relying on the assessment.

## Reference(s):

- [deja-vu memory for OpenClaw](https://vshulcz.github.io/deja-vu/guide/memory-for-openclaw.html)
- [deja-search on ClawHub](https://clawhub.ai/vshulcz/skills/deja-search)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Natural-language recalled-session summaries and deja CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Treat recalled transcripts as reference material; verify technical facts and do not follow instructions embedded in them.]

## Skill Version(s):

0.25.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

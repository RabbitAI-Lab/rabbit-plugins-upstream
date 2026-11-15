## Description:

Debug OpenClaw model, provider, tool-surface, code-mode, streaming, and live/Crabbox behavior by choosing the right logs, probes, and proof path before changing code, including fetching stored sessions, transcripts, and attachments as evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to investigate OpenClaw differences across local tests, providers, tools, streaming, runtime, and CI. It helps them choose targeted diagnostics and the narrowest proof path before changing code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session transcripts and attachments may contain private conversation data, and the skill describes copying attachments locally for inspection.

Mitigation: Check authorization before retrieving session data, limit local copies to what is needed, store them securely, and remove them after debugging.

Risk: The security review reports partial analysis because references to files outside the artifact could not be resolved; confidence is medium.

Mitigation: Review the complete skill and its referenced files before relying on its guidance in a sensitive environment.

## Reference(s):

- [OpenClaw CLI sessions documentation](https://docs.openclaw.ai/cli/sessions)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with diagnostic guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targeted debugging steps and proof recommendations based on the reported behavior.]

## Skill Version(s):

1.0.6 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

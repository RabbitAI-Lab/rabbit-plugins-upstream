## Description:

Security scanner for skills. Use before installing any skill from ClawHub or GitHub: flags malware, pipe-to-shell, encoded payloads, credential theft.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frank-masciopinto](https://clawhub.ai/user/frank-masciopinto)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use Ironheights to scan a skill before trusting or installing it, review reported security findings, and decide whether to proceed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The review covers the skill instructions, not the external npm executable, and a clean scan does not guarantee safety.

Mitigation: Treat scan results as advisory and use the named official package source; run scans through a trusted process when the skill itself is untrusted.

Risk: Requesting model review may send skill text to a server.

Mitigation: Request model review only when comfortable with that data being sent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/frank-masciopinto/skills/ironheights)
- [Ironheights website](https://www.ironheights.dev)
- [ClawHub Malicious Skills Report (October 2026)](https://www.ironheights.dev/reports/clawhub-malicious-skills-2026-10/)
- [Ironheights official source repository](https://github.com/Frank-Masciopinto/ironheights)

## Skill Output:

**Output Type(s):** [Security analysis, Guidance, Shell commands]

**Output Format:** [Markdown guidance with inline shell commands and scanner JSON summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory findings for user review.]

## Skill Version(s):

1.5.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

MetatextAI connector skill for reading, creating, and updating MetatextAI data through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect MetatextAI action schemas, evaluate chat transcripts against configured guardrails, list and create guardrail policies, and run red-team test scans through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer commands for the oo CLI.

Mitigation: Review installer commands before use, prefer verified official documentation or a package manager, and do not let an agent run the remote installer automatically.

Risk: Transcript evaluation can send chat content to the connected MetatextAI service.

Mitigation: Evaluate only authorized transcripts and remove unnecessary secrets or personal data before submission.

Risk: Policy creation changes guardrail configuration in the connected MetatextAI application.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-metatextai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [MetatextAI homepage](https://metatext.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call MetatextAI connector actions through the oo CLI after checking live action schemas.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

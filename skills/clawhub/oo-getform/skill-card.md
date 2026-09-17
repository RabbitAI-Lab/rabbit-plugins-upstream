## Description:

Getform helps agents inspect Getform action schemas, list form submissions, and submit protected forms through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Getform through OOMOL's oo CLI, including reading submissions and submitting protected forms after reviewing the live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to execute unverified remote installer scripts.

Mitigation: Do not let an agent run curl|bash or irm|iex setup commands automatically; prefer a verified installer, pinned release, or checksum/signature workflow.

Risk: OOMOL mediates Getform access and injects credentials server-side.

Mitigation: Install only when this access model is acceptable, and review the connected account scope before use.

Risk: The submit_form action can create new Getform submissions.

Mitigation: Confirm the exact submit_form payload and intended effect with the user before running the write action.

## Reference(s):

- [Getform skill on ClawHub](https://clawhub.ai/oomol/skills/oo-getform)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Getform homepage](https://forminit.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON payloads for oo connector commands and confirmations for write actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

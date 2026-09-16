## Description:

Faktoora (faktoora.com) supports reading, creating, updating, and deleting Faktoora data through the OOMOL connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage Faktoora projects through an OOMOL-connected account, including listing, retrieving, creating, updating, deleting, attaching documents, and detaching documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes one-line remote installer commands for the oo CLI.

Mitigation: Prefer a reviewed, pinned, or package-manager installation path, or independently verify OOMOL's installer source and integrity before use.

Risk: Write and destructive actions can change or delete Faktoora project data.

Mitigation: Inspect the live action schema first, then confirm the exact payload, target, and expected effect with the user before running state-changing actions.

Risk: Faktoora access is mediated through OOMOL-connected account infrastructure.

Mitigation: Use the skill only when the user is comfortable with OOMOL mediating access and has intentionally signed in and connected Faktoora.

## Reference(s):

- [Faktoora homepage](https://faktoora.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-faktoora)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

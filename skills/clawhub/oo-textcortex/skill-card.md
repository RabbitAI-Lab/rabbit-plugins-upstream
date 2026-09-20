## Description:

TextCortex lets an agent operate TextCortex through an OOMOL-connected account to create non-streaming chat completions and inspect available model metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to route TextCortex tasks through an OOMOL-connected account, including creating chat completions and listing or retrieving model information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require installing the external OOMOL oo CLI before use.

Mitigation: Review the OOMOL install guide or installer contents before running the installer, and confirm the source is expected.

Risk: TextCortex access is mediated through OOMOL-managed credentials.

Mitigation: Use the skill only when OOMOL is an acceptable intermediary and avoid storing raw TextCortex tokens locally.

Risk: Write or destructive connector actions could change or remove TextCortex data if added in the future.

Mitigation: Confirm exact payloads and effects with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [TextCortex homepage](https://textcortex.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-textcortex)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses schema-first action payload guidance and returns TextCortex connector results as JSON when actions are run.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

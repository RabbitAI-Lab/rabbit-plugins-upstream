## Description:

ImageTranslate.AI lets an agent translate text in public images through an OOMOL-connected ImageTranslate.AI account while preserving the selected layout style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate text in public images from an OOMOL-connected ImageTranslate.AI account and retrieve rendered PNG results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image translation sends image content through OOMOL/ImageTranslate.AI and may incur account charges.

Mitigation: Install only when that processing and billing model is acceptable, and require explicit confirmation before running translate_image.

Risk: The skill includes one-line remote installer commands for the oo CLI.

Mitigation: Do not let an agent run remote installer pipelines automatically; install the oo CLI through a verified, user-controlled process.

Risk: The paid translate_image operation is presented as safe/read-only despite producing billable processing.

Mitigation: Confirm the exact image URL, payload, expected effect, and account readiness before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-imagetranslate-ai)
- [ImageTranslate.AI Homepage](https://imagetranslate.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Markdown guidance with bash commands and JSON payloads; action output is JSON with rendered PNG results available through transit storage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Rendered PNG results may be up to 50 MB and ImageTranslate.AI may charge before oversized output is rejected.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

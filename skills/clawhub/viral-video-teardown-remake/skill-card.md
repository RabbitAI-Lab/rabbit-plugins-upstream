## Description:

Analyzes a short-video reference and adapts its structure into a new shot list, narration, and video assets for the user's subject.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use a reference video or social post to study its hook and pacing, then plan and produce an original short-form remake for their own product or topic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Beatra device login can spend credits and access multiple media-generation capabilities.

Mitigation: Install only if you trust Beatra with these permissions, review account and wallet access, and confirm paid actions before submitting them.

Risk: The bundled client automatically replaces package files when a newer release is available.

Mitigation: Review updates before use or disable automatic updates with `python3 scripts/mcp_client.py update --auto off`.

Risk: Social links, comments or transcripts, uploaded media, and generated artifacts are handled by Beatra's remote service.

Mitigation: Avoid submitting sensitive or unauthorized material, and check what will be shared before approving lookups or generation.

## Reference(s):

- [Reading the reference from a link](references/reference-lookup.md)
- [Reading the reference](references/teardown.md)
- [Rewriting onto your subject](references/remake-plan.md)
- [Remake workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Image, audio, and video artifacts]

**Output Format:** [Markdown teardown and shot list, with generated media or a timecoded edit list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video output depends on the chosen remake route and approved paid generation steps.]

## Skill Version(s):

0.3.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

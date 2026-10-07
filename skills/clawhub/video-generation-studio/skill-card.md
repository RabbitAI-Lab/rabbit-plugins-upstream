## Description:

Plans, generates, edits, and extends short AI video clips from written directions, images, references, or existing footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan and produce short product videos, advertisements, social clips, and cinematic concepts from prompts or supplied media, then review and refine the delivered clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared local Device Token can spend Beatra credits across generation capabilities, while uploaded prompts and media are shared with Beatra.

Mitigation: Connect only if you trust Beatra with these materials and permissions; revoke the device in the Beatra Console when access is no longer needed.

Risk: Automatic updates can replace installed package files without separate confirmation.

Mitigation: In managed or sensitive environments, disable automatic updates with `python3 scripts/mcp_client.py update --auto off` and review updates before installing them.

## Reference(s):

- [Video Generation Studio homepage](https://beatra.ai/skills/video-generation-studio)
- [Video recipes](artifact/references/video-recipes.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with video task details and media artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation uses paid Beatra tasks; completed clips are delivered as media artifacts.]

## Skill Version(s):

0.1.9 (source: server-resolved release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

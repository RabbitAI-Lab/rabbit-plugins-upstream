## Description:

Plan, generate, edit, and extend short AI videos from written shots, images, media references, or existing footage for product, advertising, and social content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to plan and produce short product, advertising, social, and cinematic clips from prompts or supplied media, then review results before further paid edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra account token can spend credits and access other Beatra media and tool capabilities.

Mitigation: Review the requested authorization, keep credentials private, confirm each paid video stage, and revoke the device in the Beatra Console if no longer trusted.

Risk: Automatic updates can replace skill package files without a separate confirmation.

Mitigation: Disable automatic updates after installation with `python3 scripts/mcp_client.py update --auto off` if manual change control is required.

Risk: Uploaded images, audio, or video are sent to Beatra for processing.

Mitigation: Inspect inputs first and upload only media the user intends to send to Beatra.

## Reference(s):

- [ClawHub release](https://clawhub.ai/beatra-ai/skills/video-generation-studio)
- [Publisher skill page](https://beatra.ai/skills/video-generation-studio)
- [Video recipes](artifact/references/video-recipes.md)
- [Review and iteration](artifact/references/review-and-iteration.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Video artifact links]

**Output Format:** [Markdown guidance with links to generated clips and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid stages require separate confirmation; report actual delivery and billing from returned results.]

## Skill Version(s):

0.2.0 (source: server-resolved release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

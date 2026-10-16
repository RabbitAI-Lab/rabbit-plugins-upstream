## Description:

Pre-publish audience reaction check. Run any content (tweet, launch copy, pricing page, announcement, blog post) through diverse AI personas before publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kbo4sho](https://clawhub.ai/user/kbo4sho)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, founders, and content teams use Preflight to test draft social posts, launch copy, pricing announcements, blog posts, and other public content against simulated audience personas before publishing. It returns a concise publish/revise/rethink/kill verdict with engagement signals, share signals, and rewrite guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Draft content may be sent to the configured model endpoint during preflight evaluation.

Mitigation: Use a trusted or local endpoint for sensitive drafts, and avoid submitting confidential unpublished content unless the endpoint is approved.

Risk: A project-level preflight-personas.md file can change the personas used for evaluation.

Mitigation: Review project persona files before using this skill automatically on repositories or workspaces you do not trust.

Risk: Persona reactions are simulated and may give misleading confidence about real audience behavior.

Mitigation: Treat the verdict as editorial guidance and review important publication decisions with human judgment before release.

## Reference(s):

- [Preflight Personas](references/personas.md)
- [Preflight on ClawHub](https://clawhub.ai/kbo4sho/skills/preflight)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown-style text summary with optional JSON output from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a verdict, engagement and share rates, persona reactions, and rewrite suggestions.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

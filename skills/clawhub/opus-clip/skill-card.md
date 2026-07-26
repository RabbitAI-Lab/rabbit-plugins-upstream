## Description: <br>
The OpusClip craft skill turns long videos such as podcasts, webinars, interviews, and streams into publishable short clips with AI candidate-finding, honest triage, and a human-reviewed pipeline. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, social media teams, and agents use this skill to plan an OpusClip workflow for turning long-form recordings into reviewed short-form clips. The skill helps choose source material, configure candidate generation, triage clips, plan credit usage, apply QA checks, and route approved exports for scheduled publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unreviewed AI-selected clips may contain caption errors, misleading context, poor framing, or unfair representations of a speaker. <br>
Mitigation: Require human review and approval for every clip before publishing, including the three-question check that the clip stands alone, is fair to the speaker, and serves the audience. <br>
Risk: Treating the Virality Score as truth can lead to poor editorial decisions or automated posting based on a proprietary prediction. <br>
Mitigation: Use the score only for triage, never as a guarantee or auto-post threshold, and recalibrate against real retention data over time. <br>
Risk: Incorrect tier, API, editor, or credit assumptions may create unexpected cost or workflow failures. <br>
Mitigation: Verify current plan limits in-app, calculate source-minute usage before subscribing, trim sources before upload, and avoid claims of API automation unless the account tier supports it. <br>
Risk: Publishing clips with uncleared music, native-only effects, or missing exports can create rights and operational problems. <br>
Mitigation: Turn off auto-music for commercial posts unless rights are verified, add licensed or platform-native audio during publishing, and download exports promptly. <br>


## Reference(s): <br>
- [Opus Clip ClawHub listing](https://clawhub.ai/social-media-skills/skills/opus-clip) <br>
- [The CLIPS framework](references/the-clips-framework.md) <br>
- [Scope, distinctions & connections](references/scope-and-connections.md) <br>
- [The reality of OpusClip in 2026](references/opus-clip-2026-reality.md) <br>
- [Workflows, checklists & worked examples](references/workflows-and-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with checklists, workflow steps, QA criteria, and planning notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces planning and review guidance only; it does not execute video processing, publishing, or hidden automation.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

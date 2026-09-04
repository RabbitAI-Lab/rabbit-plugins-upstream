## Description:

Generate three contextual follow-up suggestions after AI responses, grouped as Quick, Deep Dive, and Related for /smart-followups or natural-language requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and developers use this skill to generate short, context-aware next-question suggestions after an assistant response across supported chat channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recent chat context is used to generate suggestions, which can expose sensitive conversation content to the active provider.

Mitigation: Use the skill only where the active provider's data handling is acceptable, and avoid running it on sensitive conversations unless that review is complete.

Risk: The standalone CLI can send conversation context to OpenRouter or Anthropic and requires API keys.

Mitigation: Use the CLI only with intended providers, keep keys out of shared shell startup files, and rotate or revoke exposed keys.

Risk: Auto-triggering can run suggestion generation after responses without a separate command.

Mitigation: Keep autoTrigger disabled unless users have been told the skill will run automatically after responses.

## Reference(s):

- [Smart Follow-ups on ClawHub](https://clawhub.ai/robbyczgw-cla/skills/smart-followups)
- [OpenClaw](https://openclaw.com)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Three categorized follow-up questions rendered as interactive button labels where supported or as a numbered text list.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates one Quick, one Deep Dive, and one Related suggestion from recent conversation context.]

## Skill Version(s):

2.2.0 (source: frontmatter, changelog, release evidence; released 2026-08-31)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

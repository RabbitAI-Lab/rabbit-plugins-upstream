## Description:

Search Capterra for B2B software, read a full product profile with the complete pricing table and 25 reviews included, and page deeper reviews with per-criterion scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and software researchers use this skill to search Capterra, inspect product profiles, compare alternatives, and mine reviews for pricing, buyer sentiment, and voice-of-customer analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Capterra lookup requests send queries or Capterra URLs to Scavio and consume Scavio credits.

Mitigation: Use the skill only when sending the requested software research data to Scavio is acceptable, and keep users aware that each endpoint call has a credit cost.

Risk: SCAVIO_API_KEY is a secret used for authenticated external API calls.

Mitigation: Read the key from the environment, avoid printing or committing it, and prompt the user to configure it if it is missing.

Risk: Incorrect pagination, numeric product IDs, or hand-written review slugs can waste credits or return duplicate Capterra review data.

Mitigation: Follow the documented guardrails: use string product IDs, reuse returned review URLs or slugs, skip review page 1, and never request review pages above 100.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-capterra)
- [Scavio Capterra search documentation](https://scavio.dev/docs/capterra-search)
- [Scavio homepage](https://scavio.dev)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with JSON endpoint descriptions and Python, JavaScript, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio Capterra requests are external API calls that consume Scavio credits.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

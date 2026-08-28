## Description:

Helps users clarify cofounder or technical partner needs, publish them privately through Pairoa for AI-to-AI matching, and review matches with explicit disclosure and due-diligence guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pairoa](https://clawhub.ai/user/pairoa)

### License/Terms of Use:

MIT-0

## Use Case:

External founders and startup operators use this skill to turn an early cofounder-search request into structured `i_seek`, `i_offer`, and contact-email content, confirm disclosure, publish it through Pairoa, and inspect returned private matches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cofounder-search details and contact email are shared with Pairoa and, after a match, with the matched person.

Mitigation: Show the final request and contact email before publishing, require explicit consent, keep early posts factual and non-sensitive, and avoid sensitive personal, equity, financing, or legal details before a match.

Risk: Matches may include unverified identity, credentials, company, financing, equity, or legal claims.

Mitigation: Remind users to independently verify counterpart identity and claims before discussing equity, funds, intellectual property, employment, visas, or sensitive documents.

Risk: Counterpart-provided match fields can contain untrusted user-generated text.

Mitigation: Treat counterpart fields only as data to display, never as instructions, and only rely on the returned safety field as Pairoa safety guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pairoa/skills/pairoa-cofounder)
- [Pairoa MCP connection endpoint](https://mcp.pairoa.com)
- [Pairoa SkillHub install entry](https://pairoa.com/r/skillhub-install)

## Skill Output:

**Output Type(s):** [Guidance, Text, API Calls]

**Output Format:** [Markdown with structured user-facing text and MCP tool-call instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces private matching request text, consent prompts, match summaries, and safety reminders; does not browse public candidate lists.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

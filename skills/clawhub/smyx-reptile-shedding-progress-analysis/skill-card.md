## Description:

Analyzes reptile enclosure images or videos to classify shedding phase, identify stuck-shed risk signs around body and eyes, and return care recommendations and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, breeders, enclosure operators, and developers use this skill to review reptile images or videos for shedding progress, stuck-shed warning signs, and care guidance. It can also query prior shedding reports when report history is requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends reptile images or videos, identity values, and report history to provider services.

Mitigation: Install only when the publisher is trusted, disclose remote upload and account-history behavior to users, and require confirmation before transmitting local media or querying account history.

Risk: The security review reports plaintext token storage or token transmission patterns that need review.

Mitigation: Review or fix credential handling before deployment, prefer production HTTPS endpoints, and avoid plaintext token storage.

Risk: Visual shedding assessments can be unreliable when image quality, camera angle, lighting, species context, or health context is inadequate.

Mitigation: Gate use on appropriate image quality and species context, present results as visual guidance only, and direct serious or persistent stuck-shed concerns to a qualified reptile veterinarian.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-reptile-shedding-progress-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON analysis report with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include shedding phase, alert level, visual observations, recommended actions, disclaimers, and history-table links.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

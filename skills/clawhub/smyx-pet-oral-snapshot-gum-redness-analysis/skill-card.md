## Description:

Analyzes pet oral snapshot images, videos, or media URLs through cloud APIs to report visible gum color, gum redness, tartar coverage, oral-health observations, and report links without providing veterinary diagnosis or treatment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet-care product teams, and developers can use this skill to submit pet mouth-opening snapshots or videos for structured oral-health observations. It is intended for pet cameras, smart pet products, and pet health-management workflows that need early visual cues about gum redness and tartar, not clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media, private media URLs, platform identifiers, and report history are sent to LifeEmergence/Smyx cloud services.

Mitigation: Install and run the skill only when the publisher and backend are trusted for that data, and avoid submitting sensitive or unnecessary media.

Risk: The skill can silently create or reuse a managed user identity and tie historical reports to that identity.

Mitigation: Review identity handling before deployment, protect local state and tokens, and disclose report-history behavior to users where required.

Risk: Configuration evidence includes a development environment posture and plaintext HTTP endpoints for some services.

Mitigation: Switch configuration away from `env: dev` and require HTTPS for every endpoint that carries credentials, identifiers, media, or report data.

Risk: Service tokens or API keys may be stored locally if operators place real secrets in local configuration files.

Mitigation: Use a managed secret store or runtime environment variables, restrict file permissions, and avoid storing real secrets in `data/smyx-api-key.txt`.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-oral-snapshot-gum-redness-analysis)
- [Publisher Profile](https://clawhub.ai/user/18072937735)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and JSON-like structured text with oral-health observations and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are pet oral-care observations only and should not be treated as veterinary diagnosis or treatment.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

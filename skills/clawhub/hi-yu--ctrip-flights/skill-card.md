## Description:

Searches domestic flight tickets in China through Ctrip, including prices, airline options, schedules, province-to-city expansion, and low-price calendars.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hi-yu](https://clawhub.ai/user/hi-yu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-assistance agents use this skill to query and compare domestic China flight options by city, IATA code, or province. It can return concise Markdown tables for chat responses or structured JSON for downstream processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HTTPS certificate verification is disabled for Ctrip requests.

Mitigation: Enable normal TLS certificate and hostname verification before regular use, and reject connections that fail validation.

Risk: The skill depends on reverse-engineered Ctrip anti-bot signing behavior and an obfuscated signing artifact.

Mitigation: Review the integration for legal, compliance, and operational acceptability, and pin and integrity-check the signing artifact before deployment.

Risk: Ctrip cookie material is cached locally by the script.

Mitigation: Store the skill in a restricted workspace, avoid exposing cache files in logs or shared artifacts, and clear the cache when no longer needed.

Risk: The required quickjs dependency is not pinned in the artifact instructions.

Mitigation: Pin the dependency version and verify package integrity in the deployment environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hi-yu/skills/ctrip-flights)
- [Skill instructions](artifact/SKILL.md)
- [Flight search script](artifact/scripts/ctrip_flight.py)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, code, guidance]

**Output Format:** [Markdown tables by default, with optional structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include route summaries, best-route recommendations, direct and transfer flight details, prices, and low-price calendars.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Finds lapsed Chinese invention patents by technical topic, groups them by lapse status, and flags cases needing further verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Inventors, researchers, and small businesses use the skill to identify potentially reusable Chinese patent disclosures, review lapse reasons and related active patents, and prepare a shortlist for legal-status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries and technical descriptions are sent to PatentMax; confidential inventions or trade secrets may be disclosed.

Mitigation: Obtain approval before sending sensitive material and avoid including trade secrets in queries.

Risk: The client automatically obtains and stores a trial API key and cache files locally.

Mitigation: Review local credential persistence under ~/.patentmax and use only in environments where it is acceptable.

Risk: A configurable service URL could route queries or credentials to an unintended endpoint.

Mitigation: Keep PATENTMAX_BASE_URL fixed to the intended PatentMax service.

Risk: A lapsed patent does not establish freedom to operate; legal status may lag official records and related patents may still be active.

Mitigation: Verify status in the official Chinese patent register and seek professional freedom-to-operate review before commercial use.

Risk: The bundled client supports broader patent-search functions than the advertised Chinese lapsed-patent workflow.

Mitigation: Review requested operations and limit use to the searches and exports needed for this task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/expired-patent-finder)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [PatentMax API reference](references/api-reference.md)
- [Patent search workflow](references/search-workflow.md)
- [Query syntax](references/query-syntax.md)

## Skill Output:

**Output Type(s):** [Text, CSV files]

**Output Format:** [Chinese-language summary and UTF-8 CSV patent shortlist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes publication numbers, lapse reasons, related active patents, and verification notes.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

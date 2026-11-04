## Description:

Match provider, facility, organization or device entities across sources and resolve field conflicts using identifiers, provenance and time. Use for identity and relationship questions, including uncertain matches; a source name alone is not a matching key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redrookai](https://clawhub.ai/user/redrookai)

### License/Terms of Use:

MIT-0

## Use Case:

Data stewards, analysts, and developers use this skill to determine whether provider, facility, organization, or device records describe the same or related entities, resolve field conflicts by source and time, and document unresolved cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Records could be incorrectly merged when names or shared addresses are treated as decisive identity evidence.

Mitigation: Check identifier namespace and entity type, compare corroborating evidence, and keep ambiguous cases unresolved rather than forcing a match.

Risk: Conflicting or dated field values could be applied as current operational facts without sufficient review.

Mitigation: Use authorized records, assess source authority and relevant dates field by field, preserve provenance, and review uncertain matches before applying results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/redrookai/skills/entity-resolution)
- [Publisher profile](https://clawhub.ai/user/redrookai)
- [Worked example](artifact/references/example.md)
- [Practice](artifact/references/practice.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown, based on the requested workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a crosswalk, relationship and field decisions, unresolved cases, and a concise explanation; the skill provides guidance and makes no automatic data changes.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps creators, managers, and labels create and maintain a standards-mapped Asset Origin Record covering origin, authorship context, licensing scope, attribution requirements, source-material permissions, rights transfers, and integrity signals before publication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[otherpowers](https://clawhub.ai/user/otherpowers)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, managers, and labels use this skill before publication to create creator-held Asset Origin Records and catalog views for provenance, licensing, attribution, source-material permissions, transfers, and integrity notes. It organizes documentation and does not validate licenses, decide ownership, assess infringement, or draft legal documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat organized rights records as legal advice or as validation of ownership, licenses, or platform outcomes.

Mitigation: Treat the output as documentation only and verify legal or platform-specific claims with current official sources or counsel.

Risk: Creator-held records may preserve identities, collaborator names, signing notes, or sensitive contract details.

Mitigation: Enter sensitive details only with consent and only when comfortable preserving them in a sidecar record; avoid embedding identifying metadata unless the person chooses it.

Risk: Incomplete or self-attested records can be mistaken for verified provenance.

Mitigation: Keep unknown fields marked as not yet recorded and preserve assurance marks such as stated, documented, or signed.

## Reference(s):

- [C2PA specification 2.4 explainer](https://spec.c2pa.org/specifications/specifications/2.4/explainer/Explainer.html)
- [C2PA FAQ](https://c2pa.org/faqs/)
- [Local Contexts: About the Labels](https://localcontexts.org/labels/about-the-labels/)
- [Local Contexts: Traditional Knowledge Labels](https://localcontexts.org/labels/traditional-knowledge-labels/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown guidance plus an asset.abc.json sidecar record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The sidecar uses the otherpowers-abc/1.1 schema and marks unknown values as not yet recorded.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

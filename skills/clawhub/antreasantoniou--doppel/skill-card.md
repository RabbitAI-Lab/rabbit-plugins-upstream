## Description:

Doppel helps an agent build a consent-first, provenance-aware model of a person's own writing voice from local subject-authored material and use it to draft or revise text for the subject's review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and writing subjects use Doppel to build a local evidence pack from consented, subject-authored writing and guide an agent in drafting or revising essays, technical explanations, outreach, or social posts. The subject remains the final reviewer and approver for every generated draft.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles selected private writing and generated context packs that may contain sensitive personal data or distinctive phrasing.

Mitigation: Keep real sources, manifests, context packs, profiles, and drafts outside the repository, and choose an execution environment and model-provider data policy appropriate to the material.

Risk: Server security evidence reports that a promised Git ignore safeguard is missing.

Mitigation: Add project-specific ignore rules before using real material, keep real outputs outside the repository, and review staged files before committing.

Risk: Generated writing could be mistaken for approved publication or used for non-consensual imitation.

Mitigation: Use only subject-authored material with explicit consent, refuse third-party impersonation, label generated text as draft input, and require approval of the exact final version before attribution or publication.

## Reference(s):

- [Safety and Consent](references/safety-and-consent.md)
- [Voice Manifest Schema](schema/voice-manifest.schema.json)
- [Composition Map](docs/COMPOSITION.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown drafts, Markdown context packs, JSON manifest guidance, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated prose is draft input that requires subject ratification; context packs are local evidence, not publishable prose.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

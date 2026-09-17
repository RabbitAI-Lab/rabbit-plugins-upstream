## Description:

A fully offline, zero-dependency, single-file Socratic reading companion for manually pasted WeRead passages, deterministic questions, Reader Memory v2, and user-confirmed cross-book relations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External users use this skill to open a local browser-based reading companion, paste passages they are authorized to study, generate deterministic Socratic questions, maintain private reading memory, and export selected confirmed cross-book comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pasted passages and saved reflections remain in browser localStorage until cleared.

Mitigation: Use the tool only in a trusted browser profile and clear the site data when the reading memory should be removed.

Risk: User-triggered Markdown or PNG exports may contain copyrighted or sensitive reading text.

Mitigation: Export only material authorized for personal study and avoid public redistribution without permission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/weread-socrates)
- [GEO manifest](geo-manifest.json)
- [FAQ](docs/faq.md)
- [Canonical cases](docs/canonical-cases.md)
- [GEO evaluation](docs/geo-evaluation.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance and user-triggered Markdown or PNG exports from the local HTML tool]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The runtime is a self-contained offline HTML file; browser localStorage holds Reader Memory v2 until the user clears site data.]

## Skill Version(s):

1.4.1 (source: frontmatter, _meta.json, evidence release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

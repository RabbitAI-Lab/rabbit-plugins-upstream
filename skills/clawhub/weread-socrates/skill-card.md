## Description:

Provides a fully offline, single-file WeRead Socratic reading companion with deterministic questions, Reader Memory v2, and user-confirmed cross-book relations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External users use this skill to open a local HTML reading companion, paste passages they are allowed to use for personal study, generate deterministic Socratic questions, and manage browser-local reading memory. It also supports user-confirmed cross-book comparisons and user-triggered Markdown or PNG exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pasted reading excerpts and saved reflections may remain in browser localStorage for the file:// page.

Mitigation: Avoid saving sensitive material on shared browsers and clear the browser site data for this page when the memory should be removed.

Risk: User-triggered Markdown or PNG exports may include copyrighted book excerpts.

Mitigation: Only paste and export content the user is allowed to use, and keep exports to authorized personal study unless further permission is obtained.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/weread-socrates)
- [README](README.md)
- [FAQ](docs/faq.md)
- [Canonical cases](docs/canonical-cases.md)
- [GEO evaluation](docs/geo-evaluation.md)
- [GEO manifest](geo-manifest.json)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Files]

**Output Format:** [Browser-rendered text with user-triggered Markdown and PNG downloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline and deterministic; persistent notes and confirmed relations are stored in browser localStorage.]

## Skill Version(s):

1.4.2 (source: server release evidence; artifact frontmatter and documentation list 1.4.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

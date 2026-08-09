## Description:

Convert Persian RTL PDF slide decks into offline-first accessible HTML bundles with PyMuPDF extraction, rendering, QA gates, fidelity audit, RTL handling for mixed Persian and English numbers, searchable NFKC normalization, figure filtering, ZIP verification, and a manifest template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, and agents use this skill to transform authorized Persian RTL educational PDF slide decks into accessible offline HTML study-guide bundles. It is intended for local, fidelity-first processing with QA reporting and packaging for review or distribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package documentation claims executable workflow scripts that are not present in the artifact.

Mitigation: Verify the installed file list before relying on automation, run only bundled files from the current package, and treat missing scripts as a blocker rather than substituting similarly named files.

Risk: Persian PDF content may contain private, copyrighted, or unauthorized material.

Mitigation: Process only operator-authorized PDFs, keep filesystem access scoped to the working directory, and review generated logs, HTML, reports, and ZIPs before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/persian-pdf-studyguide-forge)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)
- [README.md](artifact/README.md)
- [Agent discovery card](artifact/AGENT_DISCOVERY.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code and shell-command examples plus generated local HTML, reports, manifests, assets, and ZIP packages when executed by an agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should remain local and offline-first unless the operator explicitly approves supplementary assets.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

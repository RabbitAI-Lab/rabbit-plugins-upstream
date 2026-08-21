## Description:

Classifies batches of Chinese standards PDFs by standard level and domain, organizes them into folders, and generates CSV inventories, offline HTML reports, and filtered ZIP exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeffm2020](https://clawhub.ai/user/jeffm2020)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, standards librarians, and operations teams use this skill to turn local folders of GB, industry, local, group, or enterprise standards PDFs into organized corpus folders, inventories, reports, and filtered exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the classifier without a dry run moves matching PDFs into categorized subfolders.

Mitigation: Run the classifier with --dry first and confirm CORPUS_DIR points at the intended corpus before executing the non-dry command.

Risk: Newly discovered source URLs may persist incorrect or untrusted standards-platform links if added without review.

Mitigation: Review discovered URLs before writing them into sources.json and keep the script-created backup for rollback.

Risk: Keyword-first domain matching can misclassify cross-domain standards or standards with ambiguous terms.

Mitigation: Review the generated CSV and HTML report, then adjust domains.json keyword order or per-corpus taxonomy files before rerunning.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/jeffm2020/skills/standards-corpus-classifier)
- [Source registry](references/sources.json)
- [Domain taxonomy](references/domains.json)
- [QX domain taxonomy](references/qx_domains.json)
- [National Public Service Platform for Standards Information](https://std.samr.gov.cn/)
- [National Standards Full-Text Disclosure System](https://openstd.samr.gov.cn/)
- [Industry Standards Filing Platform](https://hbba.sacinfo.org.cn)
- [Local Standards Filing Platform](https://dbba.sacinfo.org.cn)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands; generated CSV, offline HTML reports, ZIP archives, and reorganized PDF folders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3; local file moves can be previewed with --dry before changing the corpus directory.]

## Skill Version(s):

1.0.0 (source: server release, SKILL.md frontmatter, manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

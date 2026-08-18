## Description:

Generates an HTML technical R&D brief from a patent Excel file by tagging relevant patents, analyzing technology trends, companies, and categories, and preserving patent links and embedded images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT

## Use Case:

Developers, patent analysts, and technical research teams use this skill to turn a patent Excel export and topic configuration into a tagged workbook and a self-contained HTML research brief.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Topic-selected configuration files are Python modules that execute when the topic is loaded.

Mitigation: Review and trust topic config files before use, and do not run configs from untrusted publishers or unknown topics.

Risk: Install and run scripts can install Python packages, and report generation may fetch an external background image.

Mitigation: Run in a virtual environment, pin dependencies, and disable or explicitly approve network access for controlled or offline workflows.

Risk: Generated reports can include patent links, embedded images, and other potentially sensitive source data.

Mitigation: Review generated HTML and workbook outputs before sharing and apply the same confidentiality controls used for the source patent export.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yuanzhian-patsnap/skills/tech-report-skill)
- [Technical improvements](artifact/IMPROVEMENTS.md)
- [Sample data format](artifact/examples/SAMPLE_DATA.md)
- [Patsnap analytics](https://analytics.zhihuiya.com/)
- [Zhihuiya open platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; generated artifacts are Excel and self-contained HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are written next to the input Excel file and may include a tagged workbook and an HTML report.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact CHANGELOG also contains v1.1.0 dated 2026-06-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

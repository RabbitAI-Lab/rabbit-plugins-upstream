## Description:

Guides Guandata BI analysis, ETL governance, dashboard validation, and publishing through the official Guandata tools and local helpers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

Developers and BI administrators use this skill to troubleshoot Guandata data access, govern ETL pipelines, validate dashboard figures, and prepare BI content for publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Destructive ETL or page changes and SuperApp or mobile-layout publishing can affect production BI resources.

Mitigation: Require explicit itemized approval, preserve backups and source files, and check downstream references before execution.

Risk: A modified or untrusted ZIP archive could make the mobile-layout helper unsafe to use.

Mitigation: Run the helper only on trusted guanvis-generated archives.

## Reference(s):

- [Declared project homepage](https://github.com/maojiebc/majia-guanyuan)
- [Restricted-query playbook](artifact/references/restricted-query-playbook.md)
- [Dashboard evidence guide](artifact/references/dashboard-evidence.md)
- [ETL governance guide](artifact/references/part-b-governance.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local dashboard evidence and BI configuration artifacts.]

## Skill Version(s):

3.4.1 (source: release metadata, skill metadata, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Creates an offline, self-contained finance and industry news war-map HTML from real searched news, with geolocated ECharts points, China/world views, filters, hover details, and a data-driven executive suggestions panel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[forrestneo](https://clawhub.ai/user/forrestneo)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, developers, and finance leaders use this skill to turn real recent finance or industry news into a geospatial intelligence map and executive recommendation panel. It supports search-to-fill workflows, deduplication, local XLSX data management, and generation of a shareable offline HTML report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated report embeds web-derived news data into HTML/JavaScript, which can carry unsafe or misleading content if inputs are untrusted.

Mitigation: Use trusted or sanitized news inputs before opening or sharing the generated HTML report.

Risk: The skill can create or overwrite news.xlsx and the generated HTML report in the directory where it is run.

Mitigation: Run it from a dedicated project directory and review existing files before build, merge, replace, or fill operations.

Risk: Optional Supabase pull/push commands synchronize data with a remote database using user-provided credentials.

Mitigation: Treat remote synchronization as opt-in, review config.toml before use, and avoid storing broader credentials than needed.

## Reference(s):

- [Server-resolved source repository](https://github.com/forrestneo/finance-news-warmap)
- [ClawHub skill page](https://clawhub.ai/forrestneo/skills/finance-news-warmap)
- [README](artifact/README.md)
- [Build pipeline](artifact/references/build.py)
- [Search and fill pipeline](artifact/references/pipeline.py)
- [Supabase configuration example](artifact/references/config.example.toml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, JSON-compatible news data, XLSX data files, and generated offline HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces news.xlsx and a self-contained HTML report in the current working directory; optional Supabase synchronization requires an explicit local config.toml.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

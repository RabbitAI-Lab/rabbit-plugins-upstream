## Description: <br>
Run AEO audits, preview branch audits, changed-page sitemap audits, local/private preview audits with explicit opt-in, sitemap origin rewriting, static-output audits, regression comparisons, site fixes, schema validation, and llms.txt generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arberx](https://clawhub.ai/user/arberx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, site owners, and marketing teams use AEO to audit websites, preview branches, local builds, and sitemaps for AI-search readiness, then produce reports, fixes, schema checks, llms.txt files, and regression comparisons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a third-party npm audit package against websites or local builds, which may access public, staging, or private content. <br>
Mitigation: Install only if you trust @ainyc/aeo-audit and audit only sites or builds you are authorized to inspect; use --allow-local only for intended local or private targets. <br>
Risk: Fix workflows can modify project files or generated AI-access files. <br>
Mitigation: Require explicit user confirmation, review diffs, and rerun the audit before relying on changes. <br>


## Reference(s): <br>
- [AEO homepage](https://ainyc.ai) <br>
- [ClawHub skill page](https://clawhub.ai/arberx/skills/aeo) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Analysis, Markdown, Code, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands, plus JSON or agent-format audit reports when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate or update llms.txt, llms-full.txt, robots.txt, schema snippets, and site files during explicit fix workflows.] <br>

## Skill Version(s): <br>
4.4.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

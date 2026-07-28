## Description: <br>
Convert Persian RTL PDF slide decks into offline-first accessible HTML bundles with PyMuPDF extraction, rendering, QA gates, fidelity audit, RTL handling for mixed FA/EN numbers, searchable index with NFKC normalization, figure filtering, ZIP verification, and a manifest template. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and educators use this skill to convert authorized Persian RTL educational PDF slide decks into offline HTML study-guide bundles with source-text preservation, audit reports, search, QA checks, and ZIP packaging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package advertises conversion and QA scripts that are not included in the artifact. <br>
Mitigation: Verify the installed files and run the package self-test before relying on the skill for production or clinical study materials. <br>
Risk: The workflow reads local PDFs and writes generated study-guide files and archives. <br>
Mitigation: Use only authorized Persian RTL educational PDFs and run the skill in a controlled local workspace. <br>
Risk: PDF extraction, normalization, or enrichment can introduce inaccurate or misleading study content. <br>
Mitigation: Keep source text separate from added material, review generated outputs, and require measured QA evidence before sharing the guide. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/persian-pdf-studyguide-forge) <br>
- [Agent discovery card](artifact/AGENT_DISCOVERY.md) <br>
- [Build manifest template](artifact/templates/build_manifest.yaml) <br>
- [Source unit HTML template](artifact/templates/source_unit.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with code blocks and generated local HTML, asset, report, manifest, and ZIP files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Offline-first outputs for local workspaces; network use is off by default unless the operator approves supplementary local assets.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

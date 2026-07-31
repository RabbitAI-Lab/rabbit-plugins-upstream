## Description: <br>
Renders existing skill output manifests into HTML, DOCX, or PDF reports without performing data analysis or downloading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial workflow users use this skill to turn existing output-manifest.json or QA report files from other skills into deliverable HTML, DOCX, PDF, and report metadata files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security review identified under-disclosed input scanning and dependency risks. <br>
Mitigation: Install only when the manifests and input directories are trusted, and prefer an explicit --manifest path over broad --input-dir scanning. <br>
Risk: PDF rendering and optional dependencies can expand the execution and parsing surface for untrusted inputs. <br>
Mitigation: Avoid PDF generation for untrusted manifests unless rendering is sandboxed, and review or pin optional dependencies such as geoskill-data-fetcher and weasyprint. <br>
Risk: Generated conclusions are limited to the contents of the supplied manifest and may not satisfy compliance or certification needs. <br>
Mitigation: Require human review before using generated reports for compliance, certification, or other consequential decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-geospatial-report-generator) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, JSON] <br>
**Output Format:** [HTML, DOCX, PDF, and JSON report manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [DOCX and PDF output depend on optional packages; HTML is available as the default fallback.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

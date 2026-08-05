## Description: <br>
Renders HTML, DOCX, or PDF reports from local output-manifest.json or QA report inputs produced by other skills without performing analysis or downloading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and reviewers use this skill to turn existing skill output manifests or QA summaries into formatted deliverable reports for review and sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Untrusted or unsupported manifests can lead to misleading report content because the skill formats supplied local inputs without independent analysis or certification. <br>
Mitigation: Use trusted local manifests, review conclusions against the source data, and require human domain review before compliance or certification use. <br>
Risk: PDF rendering and optional document dependencies increase runtime and dependency exposure for untrusted inputs. <br>
Mitigation: Pin and vet dependencies, avoid PDF generation for untrusted manifests, and run the renderer in a restricted environment without sensitive local files or internal network access. <br>
Risk: The release under-discloses dependency behavior, including a data-fetcher dependency that is not needed for local-only report rendering. <br>
Mitigation: Remove or constrain the data-fetcher dependency when it is not needed, and install the skill only in a reviewed environment. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, HTML, DOCX, PDF] <br>
**Output Format:** [HTML, DOCX, PDF, and JSON report metadata files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Falls back to HTML when optional DOCX or PDF dependencies are unavailable; reports reflect only the supplied local manifests.] <br>

## Skill Version(s): <br>
2.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

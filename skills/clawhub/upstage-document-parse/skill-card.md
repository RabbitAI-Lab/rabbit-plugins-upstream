## Description: <br>
Parse PDFs, images, DOCX, PPTX, XLSX, HWP, and HWPX documents into layout-aware Markdown or HTML with tables, figures, headings, and bounding boxes using the Upstage Document Parse API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upstage-deployment](https://clawhub.ai/user/upstage-deployment) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document-processing teams use this skill to convert supported business documents into structured Markdown or HTML while preserving layout elements such as tables, figures, headings, and coordinates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected documents are uploaded to Upstage's remote API for processing. <br>
Mitigation: Use this skill only when third-party processing by Upstage is allowed by the user's policies and the provider's retention terms are understood. <br>
Risk: Confidential, regulated, personal, or secret documents may be exposed to a third-party service if used without policy review. <br>
Mitigation: Do not process those documents unless the organization has approved Upstage for that data class. <br>
Risk: API credentials may be exposed if embedded directly in prompts, code, or files. <br>
Mitigation: Use the UPSTAGE_API_KEY environment variable and avoid hardcoding keys in generated commands or scripts. <br>


## Reference(s): <br>
- [Upstage Document Parse Console](https://console.upstage.ai/api/document-digitization/document-parsing) <br>
- [Document Parse Sync API Detail](artifact/references/sync-options.md) <br>
- [Document Parse Async API Workflow](artifact/references/async-workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with Python or curl examples; parsed document outputs may be Markdown, HTML, text, or JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses UPSTAGE_API_KEY for authentication and prints the resolved absolute path when writing parsed output files.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

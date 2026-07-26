## Description: <br>
Convert unstructured documents into LLM-ready structured data, supporting PDF, Word, PPT, and images while extracting paragraphs, formulas, tables, charts, and other elements into reading-order Markdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paodingai](https://clawhub.ai/user/paodingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and document-processing agents use this skill to convert local PDFs, Office documents, and images into Markdown before extracting fields, tables, summaries, or validation inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected PDFs, Office files, or images are uploaded to PaodingAI/PDRouter for conversion. <br>
Mitigation: Use only documents approved for external processing, and avoid confidential or regulated documents unless that processing is authorized. <br>
Risk: The API key is required for remote conversion and should be treated as a secret. <br>
Mitigation: Provide PAODINGAI_API_KEY through the execution environment and avoid placing it in prompts, source files, or generated Markdown. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/paodingai/skills/pdflux-pdf2markdown) <br>
- [PaodingAI Platform](https://platform.paodingai.com/platform/) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown text, or JSON when the API response does not contain Markdown; optionally written to a user-specified file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and PAODINGAI_API_KEY; PAODINGAI_API_BASE_URL, PD_ROUTER_SERVICE_CODE, and PDFLUX_INCLUDE_IMAGES are optional settings.] <br>

## Skill Version(s): <br>
1.3.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

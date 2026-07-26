## Description: <br>
Shared medical document preprocessing library that loads PDF, Office, spreadsheet, text, JSON, CSV, and image files into normalized text, page, JSON, or table artifacts for downstream skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers building medical-document skills use it to normalize clinical files before downstream extraction, review, or generation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Medical documents may contain sensitive health information. <br>
Mitigation: Use the skill only in environments that meet applicable privacy, retention, and access-control requirements. <br>
Risk: Parsing legacy Office files, PDFs, or images may require external conversion or OCR tools. <br>
Mitigation: Run LibreOffice, PDF tooling, and OCR dependencies in a constrained environment, especially for untrusted inputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/doc-preprocess) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, configuration, guidance] <br>
**Output Format:** [Python library outputs normalized artifact dictionaries and Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Artifact dictionaries use kind values such as text, pages, json, and tables.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

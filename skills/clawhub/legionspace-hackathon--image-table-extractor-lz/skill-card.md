## Description: <br>
Extracts table data from user-provided images and returns the preserved results as Markdown tables and CSV. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and operations teams use this skill to extract visible tables from uploaded images, filter only explicit pass or 通过 cells, and provide matching Markdown and CSV outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded images may be sent to a third-party Ketop endpoint, which can expose confidential screenshots, regulated records, personal data, or proprietary tables. <br>
Mitigation: Use only images approved for that service and avoid sensitive data unless consent, retention, and privacy handling are documented. <br>
Risk: The skill uses an API key for the Ketop service. <br>
Mitigation: Store KETOP_KEY_TOKEN through a proper secret mechanism and avoid pasting it into chat, logs, or persistent files. <br>
Risk: Image table extraction may misread, omit, or reorder cells in complex or low-quality images. <br>
Mitigation: Review the Markdown table and CSV against the source image before relying on the extracted data. <br>


## Reference(s): <br>
- [Image Table Extraction Reference](references/img-table.md) <br>
- [CSV Format Reference](references/csv-format.md) <br>
- [Ketop Image Table API Endpoint](https://kpp.ketop.cn/Api/KpAiImgTbApi?act=imgtb) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown] <br>
**Output Format:** [Markdown table plus CSV code block] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preserves visible table data and headers; removes only cells explicitly marked pass or 通过.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

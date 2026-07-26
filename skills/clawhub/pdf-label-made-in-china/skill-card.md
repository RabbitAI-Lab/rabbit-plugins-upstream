## Description: <br>
Adds "Made In China" text in batch to Amazon FBA product label PDFs, aligning the text below a selected label field and centered with barcodes across single-type or mixed-label files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hipeterjiang](https://clawhub.ai/user/hipeterjiang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operations teams, and agents use this skill to add country-of-origin text to Amazon FBA label PDFs, preview placement when needed, and produce modified PDFs for delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill instructs agents to run an unpinned dependency install with sudo. <br>
Mitigation: Install dependencies in a controlled environment without sudo where possible, pin reviewed package versions, and avoid changing system Python packages during routine use. <br>
Risk: The workflow depends on an add_made_in_china.py script that is not included in the reviewed artifact. <br>
Mitigation: Confirm the script is present, reviewed, and trusted before processing business labels or user-supplied PDFs. <br>
Risk: Incorrect y-position or barcode mapping can place the country-of-origin text incorrectly on labels. <br>
Mitigation: Generate a test page for uncertain layouts and inspect the first and last output pages before delivery. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hipeterjiang/skills/pdf-label-made-in-china) <br>
- [Server-resolved source repository](https://github.com/hipeterjiang/pdf-label-made-in-china) <br>
- [Server-resolved source commit](https://github.com/hipeterjiang/pdf-label-made-in-china/commit/3a907960e3b045068520e0eab814a58d966a5593) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with bash command examples and modified PDF file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses user-provided PDF paths, barcode values, y-position settings, optional multi-barcode mappings, and optional test-page generation.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

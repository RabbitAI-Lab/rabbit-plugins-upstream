## Description: <br>
This skill helps agents locally deconstruct insurance product documents into structured Markdown reports for an Obsidian insurance product library. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lzquinn](https://clawhub.ai/user/lzquinn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Insurance advisors, analysts, and knowledge-base maintainers use this skill to process a local product-material directory, extract evidence from PDFs and spreadsheets, and produce a standardized product deconstruction report for comparison and client communication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Extracted insurance product quotes and tables are stored locally in .product-cache and may also be written to a synced Obsidian vault. <br>
Mitigation: Configure config.json to use an intended staging or Obsidian folder, run the skill only on a narrow product-material directory, and review local sync settings before processing sensitive files. <br>
Risk: Repeatable installs may vary because dependency requirements are range-based rather than fully pinned. <br>
Mitigation: Pin or lock Python dependency versions before use in a controlled or production workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lzquinn/skills/insurance-product-deconstruction) <br>
- [Repository URL listed in README](https://github.com/Lzquinn/insurance-product-deconstruction.git) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, JSON evidence caches, and shell command/configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local .product-cache evidence files and can write report Markdown to the configured Obsidian output path.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

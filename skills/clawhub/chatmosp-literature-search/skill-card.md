## Description: <br>
Chatmosp Literature Search helps agents search academic literature when MOSP_database lacks matching MSR/KMC parameters and extract surface energy, adsorption energy, interaction matrix values, source details, and completeness scores. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sanyangye](https://clawhub.ai/user/sanyangye) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and researchers using ChatMOSP use this skill when parameter-builder detects missing catalyst or reaction parameters and the user chooses literature search. The skill guides article discovery, supplemental-information review, parameter extraction, validation, and handoff of a scored parameter table. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may browse academic sites and download or convert supplemental PDF files while searching for parameters. <br>
Mitigation: Use it only when literature retrieval is needed, keep downloaded files within the working environment, and document or clean up local PDF/text files according to project policy. <br>
Risk: Extracted scientific parameters can be incomplete, inaccurate, or unsuitable for the target MSR/KMC setup. <br>
Mitigation: Review DOI, title, authors, units, completeness score, and reasonability checks before accepting values; recalculate gas entropy in parameter-builder as the skill requires. <br>
Risk: The security review noted minor documentation issues around language routing and local PDF/text file handling. <br>
Mitigation: Confirm the response language and file-handling expectations during use, and have maintainers fix the language-routing/file-name mismatch in a future release. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sanyangye/skills/chatmosp-literature-search) <br>
- [Publisher profile](https://clawhub.ai/user/sanyangye) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown with structured JSON-style parameter tables, source details, completeness scores, and occasional shell command snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local supplemental-information PDF and text files during retrieval; extracted scientific parameters require user review before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

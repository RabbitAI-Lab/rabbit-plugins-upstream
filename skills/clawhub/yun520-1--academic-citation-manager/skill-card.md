## Description: <br>
Add real references and standardize citations for research papers and theses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, and academic writing assistants use this skill to retrieve bibliographic metadata, generate in-text citations and bibliographies, convert citation styles, and check citation completeness for papers and theses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Metadata lookup features can send citation titles, authors, DOI, or ISBN values to third-party services. <br>
Mitigation: Use online lookup only for citation data appropriate to share with Crossref or Open Library, and avoid submitting sensitive unpublished reference details. <br>
Risk: Retrieved bibliographic metadata and converted citation formats may be incomplete or incorrect. <br>
Mitigation: Review important references and journal-specific formatting requirements before using generated citations in final submissions. <br>
Risk: Bundled summary markdown files are documentation artifacts, not executable entry points. <br>
Mitigation: Use the documented Python API or CLI files for execution, and do not run COMPLETION_SUMMARY.md or PROJECT_COMPLETION_SUMMARY.md as code. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yun520-1/skills/academic-citation-manager) <br>
- [ClawHub metadata homepage](https://github.com/YouStudyeveryday/academic-citation-manager) <br>
- [Crossref API](https://api.crossref.org) <br>
- [Open Library Books API](https://openlibrary.org/api/books) <br>
- [Citation Style Language](https://citationstyles.org/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown, plain text, JSON, BibTeX, RIS, CSV, and Python or shell snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use local reference database files and optional online metadata lookups against Crossref or Open Library.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Search arXiv papers by keyword, author, category with full-text download and citation export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, AI/ML engineers, and developer agents use this skill to search arXiv by keyword, author, category, or paper ID and bring paper metadata, abstracts, links, and citations into research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live searches require network access to arXiv and may fail or return unavailable data when arXiv is unreachable. <br>
Mitigation: Run the skill in an environment where outbound access to arXiv is allowed and handle network failures as part of the agent workflow. <br>
Risk: The bundled CI verifier executes Python self-tests and discovered test files. <br>
Mitigation: Run ci/verify_product.py only on trusted skill directories, as recommended by the ClawHub security guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/arxiv-search) <br>
- [Publisher profile](https://clawhub.ai/user/itspremkumar) <br>
- [arXiv API endpoint](http://export.arxiv.org/api/query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Plain text CLI output with paper metadata, abstracts, URLs, and citation-oriented snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access to the public arXiv API for live searches; no API key is required.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

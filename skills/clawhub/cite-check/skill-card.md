## Description: <br>
Confirm every citation in a draft is real before it ships by extracting URLs and arXiv IDs, checking that they resolve, and optionally checking whether each source supports the nearby claim with a local NLI model. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workloftai](https://clawhub.ai/user/workloftai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, editors, and publishing agents use cite-check before publication to block drafts with dead or fabricated citations and to flag citations that may not support the adjacent claim. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live citation checks fetch URLs and arXiv IDs from drafts, which can reveal sensitive source lists to external sites. <br>
Mitigation: Run cite-check only in a controlled environment for confidential or embargoed drafts and avoid using it where citation URLs must remain private. <br>
Risk: Phase 2 uses local claim extraction and NLI scoring, so PARTLY, UNSUPPORTED, and UNVERIFIABLE results may require judgment. <br>
Mitigation: Treat every non-SUPPORTED result as a human review prompt before publication decisions. <br>
Risk: A non-local OLLAMA_HOST can route claim extraction outside the local machine. <br>
Mitigation: Keep OLLAMA_HOST pointed at localhost unless the deployment has approved the remote endpoint and data handling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/workloftai/skills/cite-check) <br>
- [Publisher profile](https://clawhub.ai/user/workloftai) <br>
- [Workloft Labs](https://workloft.ai/labs) <br>
- [Workloft support](https://workloft.ai) <br>
- [arXiv API endpoint](https://export.arxiv.org/api/query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and optional JSON reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Phase 1 exits non-zero when citations fail to resolve; Phase 2 exits non-zero unless cited claims are supported.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

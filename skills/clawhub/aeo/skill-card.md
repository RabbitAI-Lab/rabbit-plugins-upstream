## Description: <br>
Run AEO audits, preview branch audits, changed-page sitemap audits, local/private preview audits with explicit opt-in, sitemap origin rewriting, static-output audits, regression comparisons, site fixes, schema validation, and llms.txt generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arberx](https://clawhub.ai/user/arberx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, site owners, and marketing teams use Aeo to audit public, staging, local, or static websites for answer-engine optimization, schema quality, AI access files, and regressions, then generate prioritized fixes and related files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run a networked npm audit tool against public, staging, localhost, private, or static site targets. <br>
Mitigation: Audit local or private targets only for systems the user controls, and require explicit opt-in before using local/private access. <br>
Risk: The skill can propose or apply AEO-related file and code changes. <br>
Mitigation: Review proposed fixes before allowing writes, preserve existing site behavior, and rerun the audit when practical. <br>
Risk: Untrusted target URLs, paths, or flags could make shell execution unsafe if passed through directly. <br>
Mitigation: Validate URLs or local paths, quote each argument, pass flags as literal tokens, and reject shell metacharacters or newlines. <br>


## Reference(s): <br>
- [Aeo homepage](https://ainyc.ai) <br>
- [ClawHub skill page](https://clawhub.ai/arberx/skills/aeo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown summaries with JSON or agent-format audit results, shell commands, code/configuration changes, and generated llms.txt or robots.txt files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a networked npm audit tool and may write llms.txt, llms-full.txt, or robots.txt when the user requests generation or fixes.] <br>

## Skill Version(s): <br>
4.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

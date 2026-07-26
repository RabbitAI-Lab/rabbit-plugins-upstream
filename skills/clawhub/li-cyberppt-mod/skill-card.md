## Description: <br>
Multi-platform AI Agent Skill for generating evidence-based, editable, consulting-style PowerPoint presentations from DOCX, PDF, TXT, and XLSX inputs with staged quality gates, evidence chains, and visual QA. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[43622283](https://clawhub.ai/user/43622283) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external consultants, and developers use CyberPPT to turn source documents into evidence-traceable consulting-style presentations. The skill guides an agent through analysis, storyline planning, visual blueprinting, PPTX reconstruction, and QA review before sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes user source documents and creates local presentation artifacts. <br>
Mitigation: Use it only with documents you are comfortable processing locally, and review generated PPTX and QA artifacts before sharing. <br>
Risk: Broad presentation-related triggers may invoke the workflow when a narrower action was intended. <br>
Mitigation: Invoke it explicitly with phrasing such as "use CyberPPT" and confirm stage transitions before allowing output generation. <br>
Risk: Document and image parsing dependencies can add exposure when processing untrusted files. <br>
Mitigation: Run in a virtual environment and update parsing libraries to patched versions before opening untrusted DOCX, PDF, image, or spreadsheet inputs. <br>


## Reference(s): <br>
- [CyberPPT ClawHub Release](https://clawhub.ai/43622283/skills/li-cyberppt-mod) <br>
- [Source Analysis Reference](artifact/references/source-analysis.md) <br>
- [Storyline Reference](artifact/references/storyline.md) <br>
- [Visual System Reference](artifact/references/visual-system.md) <br>
- [PPT Production Reference](artifact/references/ppt-production.md) <br>
- [Quality Assurance Reference](artifact/references/quality-assurance.md) <br>
- [Multi-Platform Compatibility](artifact/PLATFORM_COMPATIBILITY.en.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance, command snippets, JSON or manifest records, QA reports, and editable PPTX files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate local artifacts such as evidence tables, visual blueprints, rendered slide images, validation manifests, and PowerPoint files.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

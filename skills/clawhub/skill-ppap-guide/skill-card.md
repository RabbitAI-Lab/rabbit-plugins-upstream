## Description: <br>
PPAP技能助手 helps users answer PPAP questions, generate document templates, guide form completion, and check PPAP package completeness. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality engineers, suppliers, and manufacturing teams use this skill to prepare PPAP materials, understand submission requirements, generate reusable templates, and run local completeness checks before human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PPAP requirements vary by customer and the skill is not a substitute for certification advice, customer requirements, or final engineering approval. <br>
Mitigation: Review generated guidance and templates against the applicable customer specifications and require approval from qualified quality or engineering personnel before submission. <br>
Risk: The checker focuses on completeness and format signals and may not validate the technical accuracy of PPAP content. <br>
Mitigation: Treat checker output as a preparation aid and independently verify signatures, process capability data, measurement-system results, and supporting evidence. <br>
Risk: The local checker reads supplied PPAP JSON data and can write reports to a user-selected output path. <br>
Mitigation: Run it only on intended PPAP data and choose output paths deliberately. <br>


## Reference(s): <br>
- [PPAP Knowledge Reference](references/ppap_knowledge.md) <br>
- [PPAP Template Guide](references/ppap_templates.md) <br>
- [PPAP Completion Guidance](references/ppap_guidance.md) <br>
- [PPAP FAQ and Cases](references/ppap_faq.md) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-ppap-guide) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-ppap-guide) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands] <br>
**Output Format:** [Markdown guidance, document templates, JSON or text checker reports, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The checker expects PPAP information as JSON or a JSON file path and supports submission levels 1-5.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Design, test, review, and maintain agent skills using multi-agent iterative refinement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chunhualiao](https://clawhub.ai/user/chunhualiao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent maintainers use this skill to create, review, test, refactor, and audit OpenClaw agent skills with quality gates and role-separated design, review, and testing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may direct agents to search persistent memory and notes, which can expose workspace context beyond the immediate request. <br>
Mitigation: Install it only in workspaces where that access is intended, and confirm memory use boundaries before running skill design or audit workflows. <br>
Risk: The workflow includes git commit and push steps that could publish unintended skill changes. <br>
Mitigation: Require explicit user confirmation before commits or pushes, prefer feature branches and pull requests, and review generated artifacts before publishing. <br>
Risk: The skill relies on external dependencies such as deepwiki, vector memory, OpenClaw subagents, and validation scripts. <br>
Mitigation: Verify dependencies in a controlled workspace and inspect the bundled validation scripts before allowing them to run. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chunhualiao/skill-engineer) <br>
- [Anthropic Complete Guide to Building Skills for Claude](https://claude.com/blog/complete-guide-to-building-skills-for-claude) <br>
- [Complete Guide to Building Skills for Claude PDF](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf?hsLang=en) <br>
- [References README](references/README.md) <br>
- [Designer Guide](references/designer-guide.md) <br>
- [Reviewer Rubric](references/reviewer-rubric.md) <br>
- [Tester Protocol](references/tester-protocol.md) <br>
- [Functional Tests](tests/functional-tests.md) <br>
- [Trigger Test Cases](tests/test-triggers.json) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline code blocks, checklists, file artifacts, and validation commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces validated skill artifacts and review or testing guidance; scripts may emit pass/fail results and quality scores.] <br>

## Skill Version(s): <br>
3.2.0 (source: server release metadata and skill.yml; SKILL.md metadata lists 3.6.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
